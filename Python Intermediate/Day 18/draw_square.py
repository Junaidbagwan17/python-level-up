from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.color("YellowGreen")
t.shape("turtle")
t.pencolor("black")

# Draw a Square
for i in range(4):
    t.forward(100)
    t.right(90)

s.exitonclick()
