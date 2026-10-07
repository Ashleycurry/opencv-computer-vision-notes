import cv2

img=cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 自适应阈值处理：
# 输入图像（灰度图）
# 最大值
# 自适应方法
# 阈值类型 二值化
# 块大小 5*5区域
# 常数C
img2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,5,3)

cv2.imshow("adaptive_Threshlod", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
