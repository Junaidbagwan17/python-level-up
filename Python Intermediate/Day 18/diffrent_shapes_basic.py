# Basic mehtod to print shapes with diffrent colors

from turtle import Turtle, Screen
t = Turtle()
s = Screen()

for i in range(4):
    t.left(120)
    t.pencolor("orange")
    t.forward(100)
    t.left(120)

t.setheading(360) # HERE we set bcz without it its losing direction

for i in range(4):
    t.pencolor("snow4")
    t.forward(100)
    t.right(90)

#Pentagon = 5
for i in range(5):
    t.pencolor("violet")
    t.forward(100)
    t.right(72)

side = round(360 / 6) #Hegagon =6
for i in range(6):
    t.pencolor("sienna2")
    t.forward(100)
    t.right(side)

side = round(360 / 7) #heptagon = 7
for i in range(7):
    t.pencolor("tomato")
    t.forward(100)
    t.right(side)

side  = (360/ 8) #octagon = 8
for i in range(8):
    t.pencolor("OliveDrab3")
    t.forward(100)
    t.right(side)

side = (360 / 9) #nonagon =9
for i in range(9):
    t.pencolor("plum3")
    t.forward(100)
    t.right(side)

side = (360 / 10) #decagon = 10
for i in range(10):
    t.pencolor("cyan")
    t.forward(100)
    t.right(side)

s.exitonclick()