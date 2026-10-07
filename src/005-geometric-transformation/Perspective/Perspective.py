import cv2
import numpy as np

img=cv2.imread('1.jpg')
rows, cols = img.shape[:2]
print(rows,cols)

# 透视变换 4对对应点 
# 原图像中的
pts1 = np.float32([[150,50],[400,50],[60,450],[310,450]])
# 目标图像中的
pts2 = np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])
# 计算出 3*3 透视变换矩阵
M = cv2.getPerspectiveTransform(pts1,pts2)
# 进行透视变换：原图 透视变换矩阵 输出的宽高
dst = cv2.warpPerspective(img,M,(cols,rows))

cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()
