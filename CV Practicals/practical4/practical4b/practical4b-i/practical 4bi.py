import cv2
from matplotlib import pyplot as plt
# Load the image
image_path = "C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical4/practical4b/practical4b-i/stop_sign.jpg"
imaging = cv2.imread(image_path)
# Check if image loaded correctly
if imaging is None:
    print("Error: Image not found! Check the file path.")
else:
    # Convert to grayscale
    imaging_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY)
    imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB)
    # Load the Haar Cascade XML file
    xml_path = "C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical4/practical4b/practical4b-i/stop_data.xml"
    xml_data = cv2.CascadeClassifier(xml_path)
    # Check if the XML file loaded properly
    if xml_data.empty():
        print("Error: XML file not found! Check the file path.")
    else:
        # Detect objects
        detecting = xml_data.detectMultiScale(imaging_gray, minSize=(30, 30))

        if len(detecting) > 0:
            for (x, y, w, h) in detecting:
                cv2.rectangle(imaging_rgb, (x, y), (x + w, y + h), (0, 255, 0), 9)
        # Display the image
        plt.imshow(imaging_rgb)
        plt.axis("off")  # Hide axes
        plt.show()
