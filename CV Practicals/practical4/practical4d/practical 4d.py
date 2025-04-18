import cv2
import numpy as np
import face_recognition
import os
# Resize helper function
def resize_image(image, scale=0.5):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    return cv2.resize(image, (width, height))
# Load and check if image exists
image_path_1 = "C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical4/practical4d/tonystark.jpg"
image_path_2 = "C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical4/practical4d/rdj_image.jpg"
if not os.path.exists(image_path_1) or not os.path.exists(image_path_2):
    print("Error: One or both image files not found! Check the file paths.")
    exit()
# Load images and convert color
img_bgr = face_recognition.load_image_file(image_path_1)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# Show BGR and RGB images (resized)
cv2.imshow('BGR Image', resize_image(img_bgr))
cv2.imshow('RGB Image', resize_image(img_rgb))
cv2.waitKey(0)
# Detect faces in the first image
img_modi = face_recognition.load_image_file(image_path_1)
img_modi_rgb = cv2.cvtColor(img_modi, cv2.COLOR_BGR2RGB)
faces = face_recognition.face_locations(img_modi_rgb)
if len(faces) == 0:
    print("No face detected in the first image!")
    exit()
face = faces[0]
copy = img_modi_rgb.copy()
cv2.rectangle(copy, (face[3], face[0]), (face[1], face[2]), (255, 0, 255), 2)
# Show detected face (resized)
cv2.imshow('Detected Face', resize_image(copy))
cv2.waitKey(0)
# Face recognition and comparison
train_encode = face_recognition.face_encodings(img_modi_rgb)[0]
test = face_recognition.load_image_file(image_path_2)
test_rgb = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
faces_test = face_recognition.face_locations(test_rgb)
if len(faces_test) == 0:
    print("No face detected in the second image!")
    exit()
test_encode = face_recognition.face_encodings(test_rgb)[0]
# Compare faces
match_result = face_recognition.compare_faces([train_encode], test_encode)
print("Do the faces match?", match_result[0])
# Draw rectangle on detected face and show (resized)
cv2.rectangle(img_modi_rgb, (face[3], face[0]), (face[1], face[2]), (255, 0, 255), 2)
cv2.imshow('I am Iron-Man', resize_image(img_modi_rgb))
cv2.waitKey(0)
cv2.destroyAllWindows()


#if no module found follow below steps in anaconda bash
# pip install face-recognition
# conda install -c conda-forge face_recognition
# pip install cmake dlib face-recognition opencv-python numpy

#if first method not works then try this
# conda install -c conda-forge dlib
# pip install cmake
# pip install face-recognition 
