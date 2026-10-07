# 寻找并绘制轮廓
import cv2

img=cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 阈值处理
ret, img2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 寻找轮廓：输入图像 轮廓的检测模式 近似查找轮廓的方法
contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 轮廓绘制：要绘制的图像 所有轮廓的坐标点 -1（绘制全部） 颜色 宽度（-1填满）
img3 = cv2.drawContours(img, contours, -1, (0,255,255), 1)

cv2.imshow("contours", img)
cv2.waitKey(0)    
cv2.destroyAllWindows()
