# Cartoonist

In this code we will teach, how to covert an image to cartoon. The Libraries we will be using are: -
* OpenCV-contrib 
* numpy

For this we are going to use a series of filters and image conversions which are given below: -

1. Firstly we will create a blurred version of the original image. Now, we don’t want the colours to interfere in this process but only want the boundaries to get blurred. For this, we first convert the image to gray – scale and then we apply the media blur filter.

2. Next we downscale the image and then apply bilateral filter to get a cartoon flavors and then again we upscale the image.

3. After this we will identify the edges in the image and then add this to the previously modified images to get a sketch pen effect. For this we are using adaptive threshold.

4. In the final step, we compile the final images obtained from the previous steps. 5. To run the code press ctrl+F5.

Note : - The images which will be used in this program must be in the same folder the code is saved

<p align="center">
<img src="https://github.com/ISTE-VIT/Sixth-Sense/blob/main/resources/cartoonist.png">
</p>
