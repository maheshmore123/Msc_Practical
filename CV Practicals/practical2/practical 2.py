import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load images
img1 = cv2.imread("C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical2/right.jpg")
img2 = cv2.imread("C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical2/left.jpg")
# Convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# SIFT feature detector
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)
# BFMatcher with KNN
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
# Apply Lowe's ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.5 * n.distance:
        good_matches.append(m)
if len(good_matches) > 4:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    # Compute homography
    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    # Get dimensions for output
    height, width, _ = img2.shape
    panorama_width = width + img1.shape[1]
    # Warp first image
    result = cv2.warpPerspective(img1, H, (panorama_width, height))
    result[0:height, 0:width] = img2  # Overlay second image
    # Save and display
    cv2.imwrite("C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical2/result.jpg", result)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("Stitched Panorama")
    plt.axis("off")
    plt.show()
else:
    print("Not enough keypoints found for stitching.")

#Put right image path first as input and left second
