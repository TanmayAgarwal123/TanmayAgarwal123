from PIL import Image, ImageChops
#import module and library

#include images from same folder
img1 = Image.open("projects\pig1.jpg")
img2 = Image.open("projects\pig2.jpg")

#now find differences between the images
diff = ImageChops.difference(img1, img2)

#now show the differences
img1.show()
img2.show()
diff.show()