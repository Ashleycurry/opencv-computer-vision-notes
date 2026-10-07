import cv2
import numpy as np

img = cv2.imread('1.jpg')

# 切片获得：高度 宽度 通道数
rows, cols, ch = img.shape

# 生成 3*3 仿射变换矩阵：旋转中心  旋转角度（正顺负逆）  缩放系数
M = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 0.6)

# 原图像 变换矩阵 输出图像尺寸中心
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
