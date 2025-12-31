from turtle import Turtle, Screen
s = Screen()
t = Turtle()

s.listen()
def move_forword():
    t.forward(30)
def move_backword():
    t.backward(20)
def move_counter_clockwise():
    t.right(-50)
def move_clockwise():
    t.right(30)
def clear():
    t.clear()
    t.pen()
    t.home()
    t.pendown()

s.onkey(key = "w", fun=move_forword)
s.onkey(key = "s", fun=move_backword)
s.onkey(key = "a", fun=move_counter_clockwise)
s.onkey(key = "d", fun=move_clockwise)
# s.onekey(key = "c", fun=clear_the_screen)

s.exitonclick()