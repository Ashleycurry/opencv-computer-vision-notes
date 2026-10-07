# 外接矩形
import cv2
import numpy as np

img=cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 边缘
ret, img2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
# 寻找轮廓
contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 取第二个轮廓
cnt=contours[1]
# 获取最小的外接矩形：轮廓
RotatedRect=cv2.minAreaRect(cnt)
# 获取常规的外接矩形：轮廓 
# 返回：起始坐标 宽度 高度
x,y,w,h=cv2.boundingRect(cnt)
# 获取最小外接矩形的定点坐标：最小外接矩形
box=cv2.boxPoints(RotatedRect)
# 取整
box=np.int0(box)

# 绘制轮廓
img3 = cv2.drawContours(img, [box], -1, (255,0,0), 3)
# 绘制矩形：要绘制的图像 矩形的坐标点/其中一个顶点 对角顶点 颜色 宽度（-1填充）
img4=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("BINARY", img)
cv2.waitKey(0)    
cv2.destroyAllWindows()
