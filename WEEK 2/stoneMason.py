from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    turn_left()
    go_up()
    turn_right()
    move_to_next_row()
    turn_right()
    go_down()
    turn_left()
    move_to_next_row()
    turn_left()
    go_up()
    turn_right()
    move_to_next_row()
    turn_right()
    go_down()
    turn_left()


def go_up():
    for i in range(4):
        put_beeper()
        move()
    put_beeper()

def go_down():
    for i in range(4):
        put_beeper()
        move()
    put_beeper()

def move_to_next_row():
    for i in range(4):
        move()

def turn_right():
    for i in range(3):
        turn_left()




if __name__ == '__main__':
    main()