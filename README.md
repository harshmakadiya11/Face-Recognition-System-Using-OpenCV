# Face-Recognition-System-Using-OpenCV-
This project demonstrates a real-time face recognition system built using Python's OpenCV library. The system captures video from your camera, detects faces, and matches them with pre-encoded face images stored in a local directory. Recognized faces are highlighted with a bounding box and labeled with their names.
his project is a simple Face Recognition system built using Python and OpenCV. It captures live video from your camera, detects faces, and matches them with known face encodings from a pre-defined directory of images.

Features:
Real-time face detection using OpenCV.
Face recognition by comparing live faces with pre-encoded known images.
Display of names for recognized faces in the video stream.

Requirements:

Before running the project, make sure you have the following dependencies installed:
OpenCV: For capturing video and image processing.
Pandas: For handling data operations (though in this code it's imported but not yet used).
Custom detection_of_image module: This should handle face detection and recognition.

You can install the required libraries using pip:
pip install opencv-python pandas

Installation
Clone the repository:
git clone https://github.com/harshmakadiya11/Face-Recognition-System-Using-OpenCV-.git

Install the necessary dependencies:
pip install -r requirements.txt
Ensure you have a directory of known images with labeled faces, which is loaded into the system to be used for recognition.

File Structure:
detection_of_image.py: Contains the detection class responsible for encoding known images and detecting faces.
main.py: The script that captures video from the camera and performs face recognition.
How It Works
Load Encoded Images: The system first loads and encodes known images from a specified directory.
Capture Video: It uses your default camera to capture video frames in real-time.
Face Detection & Recognition: For each frame, the system detects faces and compares them with the known encodings. If a match is found, the name of the person is displayed on the video.
Exit: The program will run continuously until you press the ESC key.
Usage
Modify the path to your directory of known images in the code:
det.load_encoding_images("D:/college/sem2/midterm/codes/known images")
Run the program:
python main.py
The camera feed will open, and recognized faces will be displayed with their corresponding names.

Example Code
python
Copy code
import cv2
import pandas as pd
from detection_of_image import detection

# Encodings of the known images
det = detection()
det.load_encoding_images("D:/college/sem2/midterm/codes/known images")

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    # Detect the faces
    face_locations, face_names = det.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

camera.release()
cv2.destroyAllWindows()
Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
