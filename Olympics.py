import turtle


screen = turtle.Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.bgcolor('tan')

t = turtle.Turtle()
t.speed(0)

t.pensize(2)

t.penup()
t.goto(-80 ,15)
t.pendown()
#circle - radius
t.pencolor('blue')
t.circle(35)
t.penup()
t.goto(-5,15)
t.pendown()
t.pencolor('black')
t.circle(35)
t.penup()
t.goto(70,15)
t.pendown()
t.pencolor('red')
t.circle(35)
t.penup()
t.goto(-45,-15)
t.pendown()
t.pencolor('yellow')
t.circle(35)
t.penup()
t.goto(30,-15)
t.pendown()
t.pencolor('green')
t.circle(35)

t.pencolor('purple')
t.penup()
t.goto(-5,125)
t.pendown()
t.write("Winter Olympics", font=("arial",30,"bold italic"),align="center" )

t.pencolor('purple')
t.penup()
t.goto(-5,-125)
t.pendown()
t.write("2026", font=("arial",30,"bold italic"),align="center" )














turtle.done()