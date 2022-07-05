from PIL import Image, ImageChops

img1 = Image.open("projects\image diff\pig1.jpg")
img2 = Image.open("projects\image diff\pig2.jpg")

diff = ImageChops.difference(img1, img2)

img1.show()
img2.show()

diff.show()
