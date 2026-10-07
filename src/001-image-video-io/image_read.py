import cv2 as cv

#灰度色彩空间
#img = cv.imread('opencv.png',cv.IMREAD_GRAYSCALE) 

img = cv.imread('opencv.png')

# 创建窗口并指定可调整大小
cv.namedWindow('test',cv.WINDOW_NORMAL)

# 设置窗口大小
cv.resizeWindow('test',400,400)

# 设置窗口标题
cv.imshow('test',img)
cv.waitKey(0)
cv.destroyAllWindows()

