# Face Detection

The objective of the program given is to detect object of interest(face) in real time and to keep tracking of the same object. Face detection using haarcascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.

The Libraries we will be using are:-
* OpenCV-contrib

To detected the face, the following steps are followed: -

1) Firstly, we initialize cascade which is just an XML file that contains the data to detect faces. We read the image and convert BGR frames to grayscale. (RGB to gray scale is done to reduce complexity as the image dimension change from 3 to single dimension).

2) After Grayscaling, we detect the number of faces and output is printed in the shell .

3) Lastly the rectangular box is drawn around the face and eyes for the different sizes of faces and eyes dimension and cv2.imshow is used to display an image in a window.

To run the code press ctrl+F5.

Note :- all the haarcascade file should be in the same folder in which the code is saved.
In case of Auto_web_using_face program all the steps remain same asface detection program only we have import webbrower and define we need to define the browser which you want open after the detection of faces.

<p align="center">
<img src="https://github.com/ISTE-VIT/Sixth-Sense/blob/main/resources/face_detection.png">
</p>

  
