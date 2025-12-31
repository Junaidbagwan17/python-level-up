import turtle
from turtle import Turtle, Screen
s = Screen()
s.setup(width=500, height=400)

t1 = Turtle(shape = "turtle")
t2 = Turtle(shape = "turtle")
t3 = Turtle(shape = "turtle")
t4 = Turtle(shape = "turtle")
t5 = Turtle(shape = "turtle")
t6 = Turtle(shape = "turtle")

t1.penup()
t1.goto(x=-230, y = -160)
t1.color("red")

t2.penup()
t2.goto(x=-230, y=-100)
t2.color("green")

t3.penup()
t3.goto(x=-230, y = -40)
t3.color("blue")

t4.penup()
t4.goto(x=-230, y = 20)
t4.color("yellow")

t5.penup()
t5.goto(x=-230, y = 80)
t5.color("black")

t6.penup()
t6.goto(x=-230, y = 145)
t6.color("purple")

s.exitonclick()