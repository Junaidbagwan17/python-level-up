from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

s =Screen()
s.setup(600,600)
s.bgcolor("gray4")
s.title("My Snake Game")
s.tracer(0) #2

snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

game_on =True
while game_on:
    s.update() # updated bcz the flicker behaviours
    time.sleep(0.1) # sleep at 0.1 sec to see effect after updt

    # Detect Collision with FOOD
    snake.move()
    if snake.head.distance(food) < 25:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # Detect collision with Tail or body part
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # elif
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

s.exitonclick()
