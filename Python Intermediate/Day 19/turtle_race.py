import random
import turtle
from turtle import Turtle, Screen
s = Screen()
s.bgcolor("ivory2")
s.setup(width=500, height=400)


user_bet = s.textinput(title="Guess the Winner", prompt="Predict the color of winning turtle")
colors = ["red", "green", "blue", "orange", "gray", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
race_on = False

for turtle_index in range(0, 6):
    new_t=Turtle(shape ="turtle")
    new_t.penup()
    new_t.color(colors[turtle_index])
    new_t.goto(x=-230, y = y_positions[turtle_index])
    all_turtles.append(new_t)

if user_bet:
    race_on = True

while race_on:

    for each_turtle in all_turtles:
        if each_turtle.xcor() > 230:
            race_on = False
            winner_color = each_turtle.pencolor()
            if winner_color == user_bet:
                print(f"You Win! the winner is {winner_color}.")
            else:
                print(f"You lose! the winner is {winner_color}.")

        moves = random.randint(0,10)
        each_turtle.forward(moves)

s.exitonclick()
