import cv2
import numpy as np

# Load the image
image_path = "C:/Users/DELL/Desktop/practicals/CV Practicals/practical4/practical4b/practical4b-iii/circle_image.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found! Check the file path.")
    exit()

cv2.imshow('Original', img)

# Convert to grayscale and apply blur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (3,3))

# Detect circles using HoughCircles
detected_circles = cv2.HoughCircles(
    gray_blurred, cv2.HOUGH_GRADIENT, 1, 20,
    param1=100, param2=50, minRadius=2, maxRadius=80
)

# Draw the detected circles
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(img, (a, b), r, (0, 255, 0), 3)  # Outer circle
        cv2.circle(img, (a, b), 1, (0, 255, 0), 3)  # Center of circle

cv2.imshow('Detected Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
