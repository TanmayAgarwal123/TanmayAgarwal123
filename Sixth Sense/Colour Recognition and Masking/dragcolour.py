import numpy as np
import cv2
def hchanged(x):
    print("H value changed")
def schanged(x):
    print("S value changed")
def vchanged(x):
    print("V value changed")
def nothing(x):
    print("value changed")
#capturing our video from the camera
cap=cv2.VideoCapture(0)
cv2.namedWindow('test')

#creating 3 trackbars for altering values of RGB
cv2.createTrackbar('H','test',0,179,hchanged)
cv2.createTrackbar('S','test',0,255,schanged)
cv2.createTrackbar('V','test',0,255,vchanged)


while(1):
    ret,frame=cap.read()
    #converting to HSV
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    k=cv2.waitKey(1)
    if k==27: #esc key
        break 

    #getting the values of trackbars
    h=cv2.getTrackbarPos('H','test')
    s=cv2.getTrackbarPos('S','test')
    v=cv2.getTrackbarPos('V','test')
    
    #assignming the values to the lower and upper range of HSV
    lower=np.array([h,s,v])
    higher=np.array([179,255,255])

    #creating a mask
    #mask=cv2.inRange(hsv,lower,higher)
    mask=cv2.inRange(hsv,higher,lower)

    #applying mask on the frame
    res=cv2.bitwise_and(frame,frame,mask=mask)

    #displaying the frame
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

cap.release()
cv2.destroyAllWindows()

