#importing necessary libraries
import cv2
import numpy as np

#reading our image
img = cv2.imread("ironman.png")
#img = cv2.imread(0)

#downscaling the image
img = cv2.resize(img, dsize=(480,480))

# 1) Edges
#converting the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blurring the image
blur = cv2.medianBlur(gray, 5) #medianBlur(source, kernel_size)
#finding edges
edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
#adaptiveThreshold(source, maxValue, adaptiveMethod, thresholdType, blockSize, Constant)

# 2) Color
color = cv2.bilateralFilter(img, 9, 300, 300)
#bilateralFilter(source, d, sigmaColor, sigmaSpace, borderType)

# 3) Cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imshow("Image", img)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("edges", edges)
cv2.imshow("color", color)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()