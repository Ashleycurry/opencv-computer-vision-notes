# 图像平滑
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 图像读取
img = cv2.imread('noise.jpg')

# 均值滤波：原图像 卷积核大小
blur1 = cv2.blur(img, (5, 5))   	
# 高斯滤波：原图像 卷积核大小 水平方向偏差 垂直方向偏差 边界填充类型
blur2 = cv2.GaussianBlur(img, (5, 5), 1) 
# 中值滤波：原图像 卷积核大小
blur3 = cv2.medianBlur(img, 5)  	 

# 图像显示
# 画布大小 分辨率
plt.figure(figsize=(10, 5), dpi=100)
# 控制正常字符显示
plt.rcParams['axes.unicode_minus'] = False
# 图像1：141代表1行4列序号1 原图像 图像标题
plt.subplot(141), plt.imshow(img), plt.title("Original")
plt.xticks([]), plt.yticks([])
# 图像2
plt.subplot(142), plt.imshow(blur1), plt.title("Mean Filtering")
plt.xticks([]), plt.yticks([])
# 图像3
plt.subplot(143), plt.imshow(blur2), plt.title("Gauss Filtering")
plt.xticks([]), plt.yticks([])
# 图像3
plt.subplot(144), plt.imshow(blur3), plt.title("Median Filtering")
plt.xticks([]), plt.yticks([])

plt.show()

