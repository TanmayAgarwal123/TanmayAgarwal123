
import cv2 
import numpy as np

cap=cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")  

mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
cap = cv2.VideoCapture(0) 

font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
weared_mask_font_color = (0, 255, 0) #GREEN
not_weared_mask_font_color = (0, 0, 255) #RED
thickness = 2
font_scale = 1

weared_mask ="Thank you for wearing mask"
not_weared_mask = "Please wear a MASK to defeat Corona"

while 1:  
    ret, img = cap.read()  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    print("number of faces found :",len(faces))
    img = cv2.flip(img,1); #to flip img for correct text
    
    for (x,y,w,h) in faces: 
        # To draw a rectangle in a face  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
         
        eyes = eye_cascade.detectMultiScale(roi_gray)  
  
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
            #Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
            
        mouth_rects = mouth_cascade.detectMultiScale(gray, 1.5, 5)
        
        if(len(mouth_rects) == 0):            
            cv2.putText(img, weared_mask , org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
        else:
            for (mx, my, mw, mh) in mouth_rects:
                if(y < my < y + h):                    
                    cv2.putText(img,not_weared_mask , org, font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)
            
    # show the images
    cv2.imshow('frame',img)
    
    # Wait for Esc key to stop 
    k = cv2.waitKey(5)
    if k == 27: 
        break
 
cap.release()
cv2.destroyAllWindows()  

