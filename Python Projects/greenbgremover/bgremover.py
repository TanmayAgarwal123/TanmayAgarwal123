import cv2
import numpy as np
video = cv2.VideoCapture("green.mp4")
image = cv2.imread("bg.jpeg")
while True:
    ret,frame = video.read()
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(frame,(640,480))
    u_green = np.array([104,153,70])
    l_green = np.array([30,30,0])
    mask = cv2.inRange(frame,l_green,u_green)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    f=frame - res
    f=np.where(f==0,image,f)
    cv2.imshow("video",frame)
    cv2.imshow("mask",f)
    if cv2.waitkey(25)==27:
        break
video.release()
cv2.destroyAllWindows()    