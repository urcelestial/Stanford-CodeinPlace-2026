from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""



def main():
    while no_beepers_present():
        move()
        check()
        distribute_beepers()
        another_beeper()
        turn_around()
        go_back()


def check():
    if beepers_present():
        pick_beeper()
        move()

def distribute_beepers():
    if no_beepers_present():
        put_beeper()
    else:
        while beepers_present():
            move()

def another_beeper():
    if no_beepers_present():
        put_beeper()

def go_back():
    while front_is_clear():
        move()
    turn_around()

def turn_around():
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()