Real Time Facial Attendance System
Overview
The Real Time Facial Attendance System is a Python-based application that automates attendance tracking by using facial recognition technology. It captures video from a webcam, detects and recognizes faces, and records attendance with a timestamp. This system aims to improve the efficiency and accuracy of attendance management in various settings, such as schools, universities, and workplaces.

Features
Real-time Capture: Uses a webcam to capture live video feed.
Face Detection and Recognition: Detects faces in the video stream and matches them against a database of known faces.
Automated Attendance: Automatically records attendance with a timestamp upon successful face recognition.
Python-Based: Developed using Python.

OpenCV: Utilizes OpenCV for video capture and image processing.

Face Recognition Library: Employs the face_recognition library for facial recognition tasks.

Tkinter: Uses Tkinter for a simple GUI message box.

Technologies Used
Python
OpenCV
face_recognition library
Tkinter

Installation
Prerequisites:
Python 3.x
pip (Python package installer)

Install dependencies:
pip install -r requirements.txt

Setup
Prepare Known Faces:
Create a directory (e.g., ImagesAttendance) to store images of the individuals whose attendance you want to track.
Organize the images in the directory, with each person's images in a separate subdirectory or named with a unique identifier.
Run face-train.py:
This script processes the images in the ImagesAttendance directory, generates facial encodings, and saves them to encodings.pkl.
This step needs to be performed before running the main attendance tracking script.
python face-train.py
Run AttendanceProject.py:
This script captures video from the webcam, detects faces, recognizes them, and records attendance.
python AttendanceProject.py

Usage
Ensure the webcam is connected and functioning correctly.
Run the AttendanceProject.py script.

The system will capture video from the webcam and display it on the screen.
When a recognized face is detected, the system will:
Mark the attendance with the person's name, date, and time.
Display a confirmation message.
The attendance data is saved in a CSV file (Attendance.csv).

Press 'q' to exit the application.

Project Structure
├── AttendanceProject.py    # Main script for real-time attendance tracking
├── face-train.py          # Script for training the face recognition model
├── ImagesAttendance/      # Directory for storing facial images
│   ├── person1/           # Subdirectory for person 1's images
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── person2/           # Subdirectory for person 2's images
│   │   ├── image3.jpg
│   │   ├── image4.jpg
│   │   └── ...
├── encodings.pkl          # File to store pre-computed face encodings
└── Attendance.csv         # CSV file to store attendance records

Contributing
Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request.

Acknowledgments
This project utilizes the face_recognition library, which is built on top of dlib.
