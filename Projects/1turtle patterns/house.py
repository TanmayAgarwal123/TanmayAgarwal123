#import turtle
import turtle


#import turtle as t
t=turtle.Turtle()
scr=turtle.getscreen()
scr.bgcolor("SkyBlue1")

#create the body of house
t.penup()
t.pensize(3)
t.color("black","yellow")
t.begin_fill()
t.goto(-200,-150)
t.pendown()
t.forward(400)
t.left(90)
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()

#create partiton
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()

#create roof
t.color("black","brown")
t.begin_fill()
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.end_fill()
t.begin_fill()
t.backward(100)
t.left(60)
t.forward(300)
t.right(60)
t.forward(100)
t.end_fill()

#create door
t.penup()
t.goto(-200,-150)
t.setheading(0)
t.pendown()
t.color("black","pink")
t.forward(230)
t.left(90)
t.begin_fill()
t.forward(90)
t.right(90)
t.forward(50)
t.right(90)
t.forward(90)
t.end_fill()
t.penup()

#create left window1
t.goto(-60,-50)
t.pendown()
t.color("black","pink")
t.begin_fill()
t.backward(50)
t.left(90)
t.forward(60)
t.right(90)
t.forward(50)
t.right(90)
t.forward(60)
t.right(90)
t.forward(25)
t.right(90)
t.forward(60)
t.backward(30)
t.right(90)
t.forward(25)
t.backward(50)
t.end_fill()


#creqte right window
t.penup()
t.setheading(270)
t.goto(100,-50)
t.pendown()
t.color("black","pink")
t.begin_fill()
t.backward(50)
t.left(90)
t.forward(60)
t.right(90)
t.forward(50)
t.right(90)
t.forward(60)
t.right(90)
t.forward(25)
t.right(90)
t.forward(60)
t.backward(30)
t.right(90)
t.forward(25)
t.backward(50)
t.end_fill()
t.penup()

#grass
t.color("black","green")
t.goto(-650,-150)
t.left(90)
t.pendown()
t.begin_fill()
t.forward(1300)
t.right(90)
t.forward(180)
t.right(90)
t.forward(1300)
t.right(90)
t.forward(180)
t.end_fill()
t.penup()

#create circle of sun
t.goto(-500,150)
t.pendown()
t.color("yellow","yellow")
t.begin_fill()
t.circle(45)
t.end_fill()
t.goto(-545,150)

#create sunrays
t.pensize(5)
for i in range(12):
        t.forward(80)
        t.backward(80)
        t.left(30)
t.penup()

#create clouds
t.goto(500,160)
t.pendown()
t.color("white","white")
t.setheading(90)
t.begin_fill()
t.circle(60,180)
t.end_fill()
t.goto(440,160)
t.setheading(90)
t.begin_fill()
t.circle(80,180)
t.end_fill()

turtle.done()
