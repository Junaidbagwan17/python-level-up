import random
import turtle
from turtle import Turtle, Screen
s = Screen()
t = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r,g,b)
    return rgb_color

t.speed(0)

for i in range(70):
    t.color(random_color())
    t.circle(100)
    t.right(35)

s.exitonclick()