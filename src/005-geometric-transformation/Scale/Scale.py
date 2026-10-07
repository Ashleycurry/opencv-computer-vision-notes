import numpy as np
import cv2 as cv

src = cv.imread('1.jpg')

# method  直接设置输出尺寸
# shape 高度 宽度 通道数
height, width = src.shape[:2] # 切片获得高度和宽度  切去通道数

# 放大 哪个 宽度调整 高度调整 插值方法：4*4像素三次样条插值
res1 = cv.resize(src, (int(1.2*width), int(1.2*height)),interpolation=cv.INTER_CUBIC)
# 缩小 同上
res2 = cv.resize(src, (int(0.6*width), int(0.6*height)),interpolation=cv.INTER_CUBIC)

cv.imshow("src", src)
cv.imshow("res1", res1)
cv.imshow("res2", res2)
print("src.shape=", src.shape)
print("res1.shape=", res1.shape)
print("res2.shape=", res2.shape)
cv.waitKey()
cv.destroyAllWindows()
