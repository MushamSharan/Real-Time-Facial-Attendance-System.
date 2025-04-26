import face_recognition
import cv2
import numpy as np
import pickle
import pandas as pd
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox

# Constants
ENCODINGS_FILE = "encodings.pkl"
ATTENDANCE_FILE = "Attendance.csv"
IMAGES_DIR = "ImagesAttendance"

# Load known face encodings
try:
    with open(ENCODINGS_FILE, "rb") as f:
        known_encodings, known_names = pickle.load(f)
except FileNotFoundError:
    print(f"Error: {ENCODINGS_FILE} not found. Please run face-train.py first.")
    exit()

# Initialize attendance dataframe
if os.path.exists(ATTENDANCE_FILE):
    attendance_df = pd.read_csv(ATTENDANCE_FILE)
else:
    attendance_df = pd.DataFrame(columns=["Name", "Date", "Time"])

# Function to show pop-up message
def show_attendance_popup(name):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Attendance Marked", f"Attendance marked for {name} ✅")
    root.destroy()

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to capture frame from camera. Exiting...")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_small_frame)

    face_encodings = []
    if face_locations:
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)

        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_names[best_match_index]
            print(f"Recognized: {name}")

            # Mark attendance if not already marked today
            now = datetime.now()
            date_string = now.strftime("%Y-%m-%d")
            time_string = now.strftime("%H:%M:%S")

            if not ((attendance_df['Name'] == name) & (attendance_df['Date'] == date_string)).any():
                new_row = {"Name": name, "Date": date_string, "Time": time_string}
                attendance_df = pd.concat([attendance_df, pd.DataFrame([new_row])], ignore_index=True)

                # SAVE immediately after marking
                attendance_df.to_csv(ATTENDANCE_FILE, index=False)
                print(f"Attendance marked for {name} at {time_string}")

                # Show pop-up message
                show_attendance_popup(name)

            # Draw rectangle and label
            top, right, bottom, left = face_location
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show the resulting image
    cv2.imshow('Attendance System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Save updated attendance (this might be redundant now as we save within the loop)
cap.release()
cv2.destroyAllWindows()