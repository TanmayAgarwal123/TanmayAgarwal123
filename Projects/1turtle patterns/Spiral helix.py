import turtle

w=turtle.Screen()
w.title('Spiral Helix')
w.bgcolor('black')

colors=['red','purple','blue','green','orange','yellow']

t=turtle.Pen()
t.speed(100)

for i in range(360):
    color=colors[i%len(colors)]
    t.pencolor(color)
    t.width(i/100 + 1)
    t.forward(i)
    t.left(59)
    #t.left(__) should be just less then 360/len(color) as this decides the number of sides of figure

turtle.done
