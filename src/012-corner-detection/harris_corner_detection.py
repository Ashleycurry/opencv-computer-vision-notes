import numpy as np
import cv2 as cv

# Harris 角点检测公式推导
def harris(image):
    # 领域中像素大小
    # 求导窗口大小
    # 自由参数
    blockSize = 2	
    apertureSize = 3	
    k = 0.04				
    
    # 颜色空间转换
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    # 角点检测：检测的图像|检测中领域像素的大小|窗口大小|自由参数
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)
    print(dst)
    
    # 获取同类型数组：元组定义返回数组形状 | 返回的数据类型
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    
    # 归一化处理：输入数组|处理后输出数组|归一化最小值|归一化最大值|归一化类型
    cv.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    
    # 循环画出归一化后的图像数组，在角区域画圆圈出
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i, j]) > 120:
                cv.circle(image, (j, i), 2, (0, 255, 0), 2)
    
    return image

src = cv.imread("test.jpg")
result = harris(src)

cv.imshow('corners', result)
cv.waitKey(0)
cv.destroyAllWindows()

