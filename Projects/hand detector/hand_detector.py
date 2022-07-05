from charset_normalizer import detect
from cvzone.HandTrackingModule import HandDetector
import cv2
import socket

cap= cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
success,img = cap.read()
h,w,_ = img.shape
detector = HandDetector(detectionCon=0.8,maxHands=2)

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1",5052)
while True:
    success,img = cap.read()
    hands, img = detector.findHands(img)
    data = []
    if hands:
        hand= hands[0]
        imlist = hand["imlist"]
        for im in imlist:
            data.extend([im[0],h - im[1],im[2]])
        sock.sendto(str.encode(str(data)),serverAddressPort)
    cv2.imshow("Image",img)
    cv2.waitKey(1)        