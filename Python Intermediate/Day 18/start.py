# from turtle import Turtle, Screen
# # https://cs111.wellesley.edu/reference/colors
# timmy_the_turtle = Turtle()
#
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.shapesize(2)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.color("DarkSeaGreen")
# timmy_the_turtle.right(90)
#
# s = Screen()
# s.screensize(400)
# s.exitonclick()


# random postitions
from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    speed = 95
    t.right(angle)
    t.fd(steps)
    t.fd(speed)
t.screen.mainloop()

