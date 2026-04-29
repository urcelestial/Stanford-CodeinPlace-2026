from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    sprint()
    pick_beeper()
    move()
    turn_left()
    sprint()
    put_beeper()
    turn_around()
    sprint()
    turn_right()
    run()
    turn_around()

def sprint():
    move()
    move()

def run():
    move()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()