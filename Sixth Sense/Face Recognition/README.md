# Face Recognition

The objective of the program given is to recognize object of interest(face) in real time. Face detection using haarcascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.

There are three steps used for recognizing faces.

Data Gathering: Gather face data (face images in this case) of the persons you want to identify. Train the Recognizer: Feed that face data and respective names of each face to the recognizer so that it can learn.
Recognition: Feed new faces of that people and see if the face recognizer you just trained recognizes them.

The Libraries we will be using are:-
* cv2: This is the OpenCV module for Python used for face detection and face recognition.

* os: We will use this Python module to read our training directories and file names.

* numpy: This module converts Python lists to numpy arrays as OpenCV face recognizer
needs them for the face recognition process.

* PIL : This is the Pillow module for Python used for importing image

Data Gathering (face_image_storer.py)

1) Firstly, we initialize cascade which is just an XML file that contains the data to detect faces. We read the image and convert BGR frames to grayscale. (RGB to gray scale is done to reduce
complexity as the image dimension change from 3 to single dimension).

2) Tocaptureauserid,“inputcommand”wasadded,thatshouldbeanintegernumber(1,2,3,etc). 3) The detectMultiScale function is a general function that detects objects. Since we are calling it on
the face cascade, that’s what it detects.
* The first option is the grayscale image.
* The second is the scaleFactor. Since some faces may be closer to the camera, they would appear
bigger than the faces in the back. The scale factor compensates for this.
 
 * The detection algorithm uses a moving window to detect objects. minNeighbors defines how many objects are detected near the current one before it declares the face found. minSize, meanwhile, gives the size of each window.

4) For each one of the captured frames, we should save it as a file on a “dataSet” directory. Each file’s name will follow the structure:
User.face_id.count.jpg

5) Run the Python script by pressing F5.


<p align="center">
<img src="https://github.com/ISTE-VIT/Sixth-Sense/blob/main/resources/face_recognintion.png">
</p>

