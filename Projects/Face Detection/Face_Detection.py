import cv2  
cap=cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
# cascade classifier is an algorithm used to detect the face, takes the xml file as input
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")  
  
# capture frames from a camera , 0 means the inbuilt camera of the system
cap = cv2.VideoCapture(0) 
  
# loop runs if capturing has been initialized. 
while 1:  # infinite loop
  
    # reads frames from a camera 
    ret, img = cap.read()  
  
    # convert to gray scale (1 layer) of each frames 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
    # Detects faces of different sizes in the input image , multi scale -> multiple faces can be detected
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #cv.CascadeClassifier.detectMultiScale(	image, scaleFactor, minNeighbors)
    #scaleFactor	Parameter specifying how much the image size is reduced at each image scale.
    #minNeighbors	Parameter specifying how many neighbors each candidate rectangle should have to retain it.
   
    print("number of faces found :",len(faces))
    for (x,y,w,h) in faces: 
        # To draw a rectangle in a face  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
  
        # Detects eyes of different sizes in the input image 
        eyes = eye_cascade.detectMultiScale(roi_gray)  
  
        #To draw a rectangle in eyes 
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
    
    # Display an image in a window 
    img1=cv2.flip(img,1)
    cv2.imshow('Lets Detect Face and Eyes',img1) 
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(5) #shows each frame at a gap of 5ms
    if k == 27: 
        break
  
# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
#cv2.destroyAllWindows()  