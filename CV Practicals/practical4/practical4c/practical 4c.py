import cv2
import imutils
# Initialize HOG descriptor and set the default people detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# Load the image
image_path = "C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical4/practical4c/Pedestrian_image.jpg"
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found! Check the file path.")
    exit()
# Resize the image for better processing
image = imutils.resize(image, width=min(400, image.shape[1]))
# Detect people in the image
(regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)
# Draw rectangles around detected people
for (x, y, w, h) in regions:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
# Display the output image
cv2.imshow("Detected Pedestrians", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# if module error "pip install imutils"