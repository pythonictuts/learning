import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(1)

for i in [0,1,2,3]:
	alex.forward(150)
	alex.left(90)

wn.exitonclick()
