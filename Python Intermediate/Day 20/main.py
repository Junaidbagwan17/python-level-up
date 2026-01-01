from turtle import Screen
import time
from snake import Snake

snake = Snake()

s =Screen()
s.setup(600,600)
s.bgcolor("black")
s.title("My snake Game")
s.tracer(0) #2

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

game_on =True
while game_on:
    s.update() # updated bcz the flicker behaviours
    time.sleep(0.1) # sleep at 0.1 sec to see effect after updt

    snake.move()

s.exitonclick()