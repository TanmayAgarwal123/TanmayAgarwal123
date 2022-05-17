import turtle
import colorsys
from cv2 import circle

turtle.bgcolor("black")
hue=0.0
turtle.hideturtle()
turtle.pensize(3)
turtle.speed(100)

for i in range(300):
    col=colorsys.hsv_to_rgb(hue,1,1)
    turtle.pencolor(col)
    hue=hue+0.009
    turtle.fd(i)
    turtle.rt(42)
    turtle.lt(18)
    turtle.circle(16)
turtle.done()  