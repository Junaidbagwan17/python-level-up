import turtle  as t_module
import random

t_module.colormode(255)
t = t_module.Turtle()
s = t_module.Screen()
color_list = [
    (226, 231, 236),
    (58, 106, 148),
    (224, 200, 109),
    (134, 84, 58),
    (223, 138, 62),
    (196, 145, 171),
    (234, 226, 204),
    (224, 234, 230),
    (141, 178, 204),
    (139, 82, 105),
    (209, 90, 69),
    (188, 80, 120),
    (68, 105, 90),
    (237, 225, 233),
    (134, 182, 136),
    (133, 133, 74),
    (63, 156, 92),
    (48, 156, 194),
    (183, 192, 201),
    (214, 177, 191)
] #list of tuples

t.speed(10)
t.penup()
t.ht()

t.setheading(225)
t.forward(300)
t.setheading(0)
total_dots = 101

for dot_counts in range(1, total_dots):

    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_counts % 10 == 0: # 10 20 30 40 then move
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

# turn left then move 50 space then turn left



s.exitonclick()