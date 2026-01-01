from turtle import Screen, Turtle
s = Screen()
s.setup(600,600)
s.bgcolor("black")


# TODO: Create a 3 Turtles Square and position like train style : M2
starting_position = [(0,0),(-20,0),(-40,0)]

for position in starting_position:
    new_segment =Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

s.exitonclick()