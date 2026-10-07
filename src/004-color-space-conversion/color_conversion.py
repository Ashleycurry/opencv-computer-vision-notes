import cv2
import numpy as np

src = cv2.imread("img.jpg")

# 原本
src = cv2.resize(src, (int(src.shape[1] / 2), int(src.shape[0] / 2)))
cv2.imshow("src", src) 

# GRAY
GRAY = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", GRAY)

# Lab
Lab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
cv2.imshow("Lab", Lab)

# Ycrcb
YCrCb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
cv2.imshow("YCrCb", YCrCb)

# cvtColor
HSV = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", HSV)


cv2.waitKey(0)
cv2.destroyAllWindows()
