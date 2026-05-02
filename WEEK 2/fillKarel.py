from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while no_beepers_present():
        sprint()
        turn_around()
        distribute_beeper()
        go_up()
    turn_right()
    sprint()


def sprint():
    while front_is_clear():
        move()

def distribute_beeper():
    while no_beepers_present():
        put_beeper()
        check()

def check():
    if front_is_clear():
        move()
    else:
        pass

def go_up():
    turn_right()
    check_again()

def check_again():
    if front_is_clear():
        move()
        turn_right()
    else:
        pass

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()