import cv2 as cv

# 一般摄像头编号都是0
cap = cv.VideoCapture(0)

while(cap.isOpened()):
    ret,frame = cap.read()
    cv.imshow('test',frame)
    # 刷新的频率 1ms
    key = cv.waitKey(1)
    if key & 0x00ff == ord('q'):
    	break

# 释放摄像头
cap.release()
cv.destroyAllWindows()
