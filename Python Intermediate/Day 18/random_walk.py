import random
from turtle import Turtle, Screen
s = Screen()
t = Turtle()

t.width(15)
t.speed(11)
random_direction = [0, 180, 270, 90]
colours = ["ForestGreen", "firebrick","DodgerBlue4","LightPink4", "ivory2", "azure3", "chocolate3", "khaki" ,"pink","red"]

for _ in range(150):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(random_direction))
s.exitonclick()
