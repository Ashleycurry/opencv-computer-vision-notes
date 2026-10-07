import numpy as np
import cv2

src = cv2.imread('1.jpg')
rows, cols, ch = src.shape # 切片获取

# 构建 2*3 变换矩阵用于仿射变换 
# [1,0,300] 表示 水平不变 向右移动（正右负左） 300
# [0,1,50] 表示 垂直不变 向下移动（正下负上） 50
M = np.float32([[1, 0, 300], [0, 1, 50]])

# 仿射变换函数：图像 变换矩阵  宽度高度
dst = cv2.warpAffine(src, M, (cols, rows))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
