import face_recognition
import os
import pickle

KNOWN_FACES_DIR = "Dataset"
ENCODINGS_FILE = "encodings.pkl"

known_encodings = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    person_dir = os.path.join(KNOWN_FACES_DIR, name)
    if not os.path.isdir(person_dir):
        continue
    for filename in os.listdir(person_dir):
        if not filename.startswith('.'):  # Ignore hidden files like .DS_Store
            filepath = os.path.join(person_dir, filename)
            try:
                image = face_recognition.load_image_file(filepath)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    known_encodings.append(encodings[0])
                    known_names.append(name)
            except Exception as e:
                print(f"Error loading image {filepath}: {e}")

with open(ENCODINGS_FILE, "wb") as f:
    pickle.dump((known_encodings, known_names), f)

print("Training completed and encodings saved.")