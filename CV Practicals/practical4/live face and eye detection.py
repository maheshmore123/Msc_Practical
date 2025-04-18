import cv2
import matplotlib.pyplot as plt

# Load Haar cascade classifiers
face_cascade = cv2.CascadeClassifier('C:/Users/DELL/Desktop/practicals/CV Practicals/practical4/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/DELL/Desktop/practicals/CV Practicals/practical4/haarcascade_eye.xml')

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)

    cv2.imshow('Live Face & Eye Detection', img)
    if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()


