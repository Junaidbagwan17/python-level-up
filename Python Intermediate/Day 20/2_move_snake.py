import time
from idlelib.configdialog import tracers
from turtle import Screen, Turtle
s = Screen()
s.setup(600,600)
s.bgcolor("black")

# TODO: Create a 3 Turtles Square and position like train style : M2
starting_position = [(0,0),(-20,0),(-40,0)]
segments =[]#2
s.tracer(0) #2

for position in starting_position:
    new_segment =Turtle("square")
    new_segment.color("white")
    new_segment.penup()#2
    new_segment.goto(position)
    segments.append(new_segment)#2

#TODO 2 :MOVE the Snake
game_on =True
while game_on:
    s.update() # updated bcz the flicker behaviours
    time.sleep(0.1) # sleep at 0.1 sec to see effect after updt

    for segnum in range(len(segments)-1, 0, -1):# the range should start at last seg then stop at first segmen and  step by -1 to till or before 0
        # also after this range specification make first segment to the new position segment
        new_x = segments[segnum-1].xcor()
        new_y = segments[segnum-1].ycor()
        segments[segnum].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

s.exitonclick()