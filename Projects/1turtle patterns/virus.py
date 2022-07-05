import turtle
turtle.speed(20)
turtle.bgcolor('black')
turtle.hideturtle()
b = 0
turtle.color('black')
turtle.left(90)
turtle.forward(120)
turtle.right(90)
turtle.color('green')
while b<10:
    turtle.right(b)
    turtle.forward(b*3)
    b=b-1