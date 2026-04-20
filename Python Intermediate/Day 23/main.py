import time
from turtle import Screen, Turtle

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

sc = Screen()
sc.setup(600, 600)
sc.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    sc.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on =False
            scoreboard.game_over()

    # detect a successful cross
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_score()

sc.exitonclick()