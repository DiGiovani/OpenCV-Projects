import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (11, 11), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("grayImg", imgGray)
cv2.imshow("blurImg", imgBlur)
cv2.imshow("cannyImg", imgCanny)
cv2.imshow("dialationImg", imgDialation)
cv2.imshow("erodedImg", imgEroded)
cv2.waitKey(0)