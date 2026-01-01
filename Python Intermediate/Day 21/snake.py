import turtle
from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0] # 1 square

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()  # 2
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0,-1):
            new_x = self.segments[segnum - 1].xcor()
            new_y = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(new_x, new_y)
        self.segments[0].forward(MOVE_FORWARD)
        # self.segments[0].left(90)

    def up(self):
        # if the current head is UP it cannot move DOWN
        if self.head.heading() != DOWN: # so when the head is not down make head then only UP
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)

    def right(self): # if it is already going to left dont allow to make RIGHT
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # def up(self):
    #     for i in self.segments:
    #         i.setheading(90)
    # def down(self):
    #     for i in self.segments:
    #         i.setheading(270)
    # def left(self):
    #     for i in self.segments:
    #         i.setheading(180)
    # def right(self):
    #     for i in self.segments:
    #         i.setheading(0)
