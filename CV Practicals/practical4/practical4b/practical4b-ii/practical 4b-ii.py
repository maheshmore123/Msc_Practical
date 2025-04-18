import cv2
import numpy as np

# Load the image
image_path = "C:/Users/DELL/Downloads/line_art_image.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found! Check the file path.")
    exit()

cv2.imshow('Original', image)

# Convert to grayscale and detect edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Detect lines using Hough Transform
lines = cv2.HoughLinesP(
    edges,
    rho=2,
    theta=np.pi / 180,
    threshold=100,
    minLineLength=20,
    maxLineGap=5
)

# Draw detected lines
line_list = []
if lines is not None:
    for points in lines:
        x1, y1, x2, y2 = points[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        line_list.append([(x1, y1), (x2, y2)])
else:
    print("No lines detected.")

# Save and display the processed image
cv2.imwrite('detectedlines.png', image)
cv2.imshow('Detected Lines', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
