# 全局阈值处理
import cv2

# 默认 bgr
img=cv2.imread('test.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 全局阈值处理：处理的图像（必须是灰度图） 设定的阈值 最大值 二值化阈值类型
#maxval设为255，所以处理后的图像是黑白图像
ret, img2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("THRESH_BINARY", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
