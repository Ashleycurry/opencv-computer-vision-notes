import cv2
import numpy as np

img = cv2.imread("1.jpg")
rows, cols, ch = img.shape

# 定义X坐标水平方向的所有像素点
mapx = np.ones(img.shape[:2], np.float32) * 200
# 定义y坐标水平方向的所有像素点
mapy = np.ones(img.shape[:2], np.float32) * 100

# 进行重映射：原图像 x像素点 y像素点 插值方式
result_img = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

cv2.imshow("img", img)
cv2.imshow("result_img", result_img)
cv2.waitKey()
cv2.destroyAllWindows()
