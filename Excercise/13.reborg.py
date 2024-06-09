
# https://reeborg.ca/reeborg.html
# 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal() :
    if right_is_clear() == True :
        turn_right()
        move()
        turn_right()
        move()
    elif front_is_clear() == True :
        move()
    elif wall_on_right() == True and wall_in_front() == True :
        turn_left()
    elif wall_in_front() == True :
        turn_left()
    