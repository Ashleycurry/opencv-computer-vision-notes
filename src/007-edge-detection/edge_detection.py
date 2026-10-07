import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('luna.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯滤波
#img_blur = cv2.GaussianBlur(img,(5,5),0)

# Canny 边缘检测
lowThreshold = 1 # 最小阈值
max_lowThreshold = 80 # 最大阈值
canny = cv2.Canny(img, lowThreshold, max_lowThreshold)

# 图像演示 大小单位：英寸
plt.figure(figsize=(8,5), dpi = 100)
plt.rcParams['axes.unicode_minus'] = False
# 图像1：141代表1行2列序号1 原图像 图像标题
plt.subplot(121), plt.imshow(img,cmap=plt.cm.gray), plt.title("Origin")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(canny,cmap=plt.cm.gray), plt.title("Edge Detection")
plt.xticks([]), plt.yticks([])

plt.show()

