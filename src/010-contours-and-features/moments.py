import cv2
img=cv2.imread('test.jpg')

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, img2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 获取轮廓
contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 取出最外围的轮廓
cnt=contours[0]
# 计算特征距：轮廓点位
m=cv2.moments(cnt)
# 计算面积：轮廓中的一个轮廓
area=cv2.contourArea(cnt)
# 周长计算：轮廓 是否闭合
perimeter=cv2.arcLength(cnt,True)

print("特证矩：",m)
print("面积：",area)
print("周长：",perimeter)

