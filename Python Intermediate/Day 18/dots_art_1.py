import random
import turtle
from turtle import Turtle, Screen
t =Turtle()
turtle.colormode(255)
s = Screen()

color_list = [
    (226, 231, 236),
    (58, 106, 148),
    (224, 200, 109),
    (134, 84, 58),
    (223, 138, 62),
    (196, 145, 171),
    (234, 226, 204),
    (224, 234, 230),
    (141, 178, 204),
    (139, 82, 105),
    (209, 90, 69),
    (188, 80, 120),
    (68, 105, 90),
    (237, 225, 233),
    (134, 182, 136),
    (133, 133, 74),
    (63, 156, 92),
    (48, 156, 194),
    (183, 192, 201),
    (214, 177, 191)
]

t.penup()
t.goto(-300, -300)

def go():
    for i in range(11):
        t.forward(50)
        t.penup()
        t.dot(20)
        t.color(random.choice(color_list))

def turn_left():
    t.penup()
    t.left(90)
    t.forward(50)
    t.setheading(180)


def turn_right():
    t.penup()
    t.right(90)
    t.forward(50)
    t.right(90)

for i in range(5):
    go()
    turn_left()
    go()
    turn_right()

s.exitonclick()

