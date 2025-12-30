# How can we Use Functions and Loops to print diffrent colors of shapes
from turtle import Turtle, Screen
import random

t = Turtle()

def draw_shape(n_sides):
    for _ in range(n_sides):
        side = 360 / n_sides
        t.forward(100)
        t.right(side)
        # t.speed(10 - n_sides)
random_colors = ["cyan", "magenta", "DarkGreen", "olive", "IndianRed", "SeaGreen"]
for i in range(3 , 11):
    t.color(random.choice(random_colors))
    draw_shape(i)

s= Screen()
s.exitonclick()