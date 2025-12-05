def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def jump2():
    if wall_in_front():
        jump()
    else:
        move()
while not at_goal():
    jump2()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
