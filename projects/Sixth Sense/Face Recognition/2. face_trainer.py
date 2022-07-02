import cv2
import os
import numpy as np
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
# How lbph works -> https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b

path='dataSet'
def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]

    for imagepath in imagePaths:
        faceImg=Image.open(imagepath).convert('L') 
        # L means -> grayscale mode-> (8-bit pixels, black and white)
        faceNp=np.array(faceImg,'uint8') #create a numpy array with integer values from the image
        ID=int(os.path.split(imagepath)[-1].split(".")[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return np.array(IDs),faces

Ids,faces=getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save('recognizer/trainingData.yml')

#A YML file is a text document that contains data formatted using YAML (YAML Ain't Markup Language), a human-readable data format used for data serialization. It is used for reading and writing data independent of a specific programming language.
# YML files are most commonly used as configuration files, which define a program or application's settings. If a program uses a YML file as a settings file, you can edit the program's settings by opening and editing the YML file in a text or source code editor. 
cv2.destroyAllWindows()
        

