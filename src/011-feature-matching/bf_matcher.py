import cv2
 
img1 = cv2.imread('test.jpg')
img2 = cv2.imread('test1.jpg')

# 初始化ORB特征点检测器
orb = cv2.ORB_create()
# 检测特征点和描述符：阈值处理图像 掩模图像（物体为黑 其余都是白的图像）
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
 
# 创建蛮力（BF）匹配器
# 对应欧式距离/汉明距离 特征点互相匹配时才能成功（默认f）
bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
 
# 匹配描述符：需要匹配的图像特征向量 被匹配的图像特征向量
matches = bf.match(des1,des2)

# 画出10个匹配的描述符
# 匹配图像1 图像1特征点 匹配图像2 图象2特征点 需要绘制的匹配点 决定绘制那些图像（空-全部绘制） 绘图的标志位（0-全部绘制 2-绘制matches中的 4-不同的绘制样式）
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
 
cv2.imshow("bf",img3)
cv2.waitKey()
cv2.destroyAllWindows()

