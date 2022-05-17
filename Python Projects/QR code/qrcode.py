import qrcode
img=qrcode.make(
    "https://google.com"
)
img.save("myqrcode.png")
img.show()
