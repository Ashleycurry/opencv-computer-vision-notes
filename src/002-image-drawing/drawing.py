import cv2
import numpy as np

img = cv2.imread("test.jpg")

# 画线 在哪绘制 起点 终点 bgr分量 线段宽度
cv2.line(img,(100,100),(100,200),(0,0,255),5)

# 画矩形 在哪画 对角线起点 对角线终点 bgr 宽度(-1实心)
cv2.rectangle(img,(200,200),(300,300),(0,255,0),5)

# 画圆 在哪画 圆心坐标 圆的半径 bgr 宽度（-1实心）
cv2.circle(img,(150,150),50,(0,0,255),5)

# 画多边形
# 多边形的各个定点
n = np.array([[10,10],[100,10],[100,100],[10,100]])
# 点的数量（自动推断） 单独的点组 [x,y]坐标
p = n.reshape((-1,1,2,))
# 在哪画 各个定点 是否闭合 bgr 宽度
cv2.polylines(img,[p],isClosed=True,color=(255,255,0),thickness=5)

# 画文本 在哪画 内容 绘制坐标（文本左上角） 文本字体 大小 文本颜色 宽度
cv2.putText(img,"I can do all thing",(150,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),5)

cv2.imshow("test",img)
cv2.waitKey()
cv2.destroyAllWindows()
