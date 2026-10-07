# 轮廓外包
import cv2

img=cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 边缘
ret, img2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
# 寻找轮廓
contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 取出第二个轮廓
cnt=contours[1]
# 轮廓外包：查找的轮廓 绘制方向（顺时针绘制True | 逆时针False）
hull=cv2.convexHull(cnt,True)
# 绘制轮廓
img3 = cv2.drawContours(img, [hull], -1, (255,0,0), 3)

cv2.imshow("hull", img)
cv2.waitKey(0)    
cv2.destroyAllWindows()
