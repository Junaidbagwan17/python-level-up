from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.color("YellowGreen")
t.shape("turtle")
t.pencolor("black")

# draw dashed line
for i in range(15):
    t.forward(5)
    t.pendown()
    t.forward(10)
    t.penup()

s.exitonclick()
