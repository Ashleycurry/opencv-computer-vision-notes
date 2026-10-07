# 多边形逼近
import cv2

img=cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 边缘
ret, img2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 寻找轮廓
contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 取出第二个轮廓
cnt=contours[1]
# 多边形逼近：查找的轮廓 精度（数字越小精度越低） 轮廓是否闭合
approxl=cv2.approxPolyDP(cnt,20,True)
# 画出轮廓
img3 = cv2.drawContours(img, [approxl], -1, (255,0,0), 3)

cv2.imshow("approx", img)
cv2.waitKey(0)    
cv2.destroyAllWindows()
