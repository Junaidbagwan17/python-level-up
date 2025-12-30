import turtle
from turtle import Turtle
import  random

turtle.colormode(255)

t = Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b) # tuple
    return rgb_color

direction = [0, 180 ,90,270]
t.width(15)

for _ in range(100):
    t.color(random_color())
    t.setheading(random.choice(direction))
    t.forward(30)