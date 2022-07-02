from skimage.metrics import structural_similarity as ssim
import imutils
import cv2

image1 = cv2.imread("pig1.png")
image2 = cv2.imread("pig2.png")
gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

(score,diff) = ssim(gray1, gray2, full=True)
diff = (diff*255).astype("uint8")
print("SSIM: {}".format(score))

thresh = cv2.threshold(diff,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts) #Grabbing contours

for c in cnts:
    (x,y,w,h) =  cv2.boundingRect(c)
    cv2.rectangle(image1,(x,y),(x+w,y+h), (0,0,255),2) #Drawing rectangle BGR thickness
    cv2.rectangle(image2,(x,y),(x+w,y+h), (0,0,255),2)  #Drawing rectangle BGR  thickness
cv2.imshow("Image-1", image1)
cv2.imshow("Image-2", image2)
cv2.imshow("Difference Between Images", diff)
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)