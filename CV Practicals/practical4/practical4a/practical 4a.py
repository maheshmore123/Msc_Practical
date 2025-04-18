import cv2
import matplotlib.pyplot as plt

# Load the image
imagePath = 'C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical4/practical4a/ind.jpg'
img = cv2.imread(imagePath)

# Check if image is loaded properly
if img is None:
    print("Error: Image not found. Check the file path!")
else:
    print("Image Loaded Successfully!")
    print("Image Shape:", img.shape)

    # Convert image to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load face classifier
    face_classifier = cv2.CascadeClassifier("C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical4/practical4a/haarcascade_frontalface_default.xml")


    # Check if classifier is loaded properly
    if face_classifier.empty():
        print("Error: Haarcascade XML file not found!")
    else:
        # Detect faces
        faces = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

        # Convert image to RGB for displaying with matplotlib
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Display the image
        plt.figure(figsize=(10, 6))
        plt.imshow(img_rgb)
        plt.axis('off')  # Hide axes
        plt.show()


#if module error "pip install opencv-python-headless"
