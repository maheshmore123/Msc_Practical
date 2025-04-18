import numpy as np
import cv2 as cv
# Termination criteria for corner refinement
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# Prepare object points (3D points)
objp = np.zeros((6*7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
# Lists to store object points and image points
objpoints = []
imgpoints = []
# Manually enter image paths
image_paths = [
    "C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical3/ChessBoard.jpeg"
    #"C:/Users/ADMIN/Desktop/chess22.jpg"
]  # Add more image paths as needed
for fname in image_paths:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    if ret:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        cv.drawChessboardCorners(img, (7,6), corners, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
cv.destroyAllWindows()
# Camera calibration
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
# Print calibration results
print("Camera matrix: ")
print(mtx)
print("Distortion coefficients: ")
print(dist)
print("Rotation Vectors: ")
print(rvecs)
print("Translation Vectors: ")
print(tvecs)
# Read an image for undistortion
undistort_img_path = "C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical3/ChessBoard.jpeg"
img = cv.imread(undistort_img_path)
h, w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
# Save the undistorted image
cv.imwrite('C:/Users/DELL/Desktop/practicals/sem2/CV Practicals/practical3/calibresult.png', dst)
print("Undistorted image saved as calibresult.png")