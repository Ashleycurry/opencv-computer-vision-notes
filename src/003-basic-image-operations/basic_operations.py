import cv2

# 1.获取图像中的像素点
img = cv2.imread("test.jpg")
# 获取像素点
px = img[200,100]
print(px)
# 获取像素点的某个通道的值
blue = img[200,100,0]
print(blue)

# 修改图像中的像素点(范围)
for x in range(500,700):
    for y in range(500,700):
    	img[x,y] = [0,0,0]

# 2.获取图像的属性
# shape 图像形状 | 彩色：行数 列数 通道数 | 黑白：行数 列数
# size	像素数目 | 彩色：行 x 列 x 通道 | 黑白：1
# dtype	数据类型
print("shape",img.shape)
print("size",img.size)
print("dtype",img.dtype)

# 3.图像通道的拆分
b,g,r = cv2.split(img)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)

# 4.图像通道的合并
img = cv2.merge((b,g,r))

# 5.颜色空间的转换
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("test1",img2)

cv2.imshow("test",img)
cv2.waitKey()
cv2.destroyAllWindows()

