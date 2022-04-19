# DRAGCOLOUR

In digital image processing and computer vision, image segmentation is the process of partitioning a digital image into multiple segments (sets of pixels, also known as image objects). The goal of segmentation is to simplify and/or change the representation of an image into something that is more meaningful and easier to analyze. 
Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images. More precisely, image segmentation is the process of assigning a label to every pixel in an image such that pixels with the same label share certain characteristics.

The libraries that are used are as following:-
Numpy opencv-contrib
Then we will create HSV track paths using command cv2.createTrackbar.
Firstly we will capture the image by using our primary camera and the
 output of that capture image will be shown on the window called “Test”.
 
 
As we have already made the trackbars in the previous step now we will
 store the positions of trackbar in the variables. In this case it is h, s, and v.
 Now we will give 2 conditions one for the upper range of the hsv and the
other lower range of the hsv and obtain the pixels lying between these
ranges and the pixels outside the ranges will become black due to bitwise
operations.
Now we will be showing the obtained pixels in a new window called res by
 applying the mask which we defined earlier!
 
<p align="center">
<img src="https://github.com/ISTE-VIT/Sixth-Sense/blob/main/resources/masking1.png">
</p>

<p align="center">
<img src="https://github.com/ISTE-VIT/Sixth-Sense/blob/main/resources/masking2.png">
</p>
