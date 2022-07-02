# Find Difference in Images

In this program you will explore how OpenCV can be used find and highlight the differences between 2 images.
The Libraries we will be using are:-
* OpenCV-contrib  Imutils
* scikit-image

1) After importing all the library, we need to read the images from the disk, assuming the images are in the same folder as the code, else you need to provide the path to the images.

2) We load our first and second images storing them as image1 and image2, respectively and then the images are converted in grayscale.

3) Using the “compare_ssim” function from scikit-image, we calculate a score and difference image, diff. The score represents the structural similarity index between the two input images. This value can fall into the range [-1, 1]. The diff image contains the actual image differences between the two input images. The difference image is currently represented as a floating- point data type in the range [0, 1] so we first convert the array to 8-bit unsigned integers in the range [0, 255].

3) Then the threshold of diiff image calculated by the function cv2.threshold and its 0 i.e its blacks and 255 it is purely white.

4) we loop over our cont and the bounding box is computed around the counter which is store as x and y and as width(w)/height(h) of the rectangle.

5) The cv2.rectangle command is used to create the rectangle box on each image. 6) cv2.imshow is used the output window in different window.
To run the code press ctrl+F5.
Note: - All the images which are going to used should be in the same folder in which the code is saved.
  
<p align="center">
<img src="https://github.com/ISTE-VIT/Sixth-Sense/blob/main/resources/ing_diff.png">
</p>
