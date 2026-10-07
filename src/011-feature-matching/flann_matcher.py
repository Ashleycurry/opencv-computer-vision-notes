# 最近邻匹配 FLANN库——高维向量的近似最近邻搜索算法
import numpy as np
import cv2 as cv

# 索引图像
img1 = cv.imread('test.jpg', cv.IMREAD_GRAYSCALE)
# 训练图像
img2 = cv.imread('test1.jpg', cv.IMREAD_GRAYSCALE)    
 
# 初始化ORB特征点检测器
orb = cv.ORB_create()
 
# 基于ORB找到关键点和描述符
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# FLANN的参数
FLANN_INDEX_LSH = 6
# 使用指定的算法
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2
# 索引中的树应递归遍历的次数（值越高精度高）
search_params = dict(checks=50)   # 或传递一个空字典
flann = cv.FlannBasedMatcher(index_params,search_params)

# 最近邻匹配：需要匹配的图像 | 被匹配的图像 | 返回最佳匹配的数量
matches = flann.knnMatch(des1,des2,k=2)

# 绘制 最近临匹配的图像
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None)

cv.imshow("flann",img3)
cv.waitKey()
cv.destroyAllWindows()

