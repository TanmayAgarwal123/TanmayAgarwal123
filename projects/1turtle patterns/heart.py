import turtle
pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def txt():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color('lightgreen')
    pen.write("I LOVE YOU ",font=("verdana",12,"bold"))
    pen.left(140)
    pen.color('red')
    pen.forward(25)
    pen.color('lightgreen')
    pen.ht()
    while True:
        pen.forward(70)
        pen.right(90)
        pen.forward(1)
        pen.right(90)
        pen.forward(70)
        pen.right(90)
        pen.forward(1)
        pen.right(90)
        
heart()
txt() 
