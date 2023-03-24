import turtle

s = turtle.getscreen()
t = turtle.Turtle()

color1 = "#ffffff"

turtle.bgcolor('black')

t.speed(10)

t.up()
t.right(90)
t.forward(100)
t.left(90)

t.fillcolor(color1)
t.begin_fill()
t.down()
t.color('silver')
t.circle(100)
t.end_fill()

t.fillcolor('black')
t.begin_fill()
t.up()
t.left(90)
t.forward(5)
t.right(90)
t.down()
t.circle(95)
t.end_fill()
t.circle(95, 60)

for i in range(3):
    if i==1:
        t.fillcolor('black')
    else:
        t.fillcolor(color1)
    t.circle(95, 120)
    x = t.xcor() 
    y = t.ycor()
    t.begin_fill()
    t.left(90)
    t.forward(95)
    t.right(120)
    t.forward(15)
    t.goto(x,y)
    t.left(30)
    t.end_fill()

for i in range(3):
    if i==0 or i==2:
        t.fillcolor('black')
    else:
        t.fillcolor(color1)
    t.circle(95, 120)
    x = t.xcor() 
    y = t.ycor()
    t.begin_fill()
    t.left(90)
    t.forward(95)
    t.left(120)
    t.forward(15)
    t.goto(x,y)
    t.left(150)
    t.end_fill()


turtle.done()