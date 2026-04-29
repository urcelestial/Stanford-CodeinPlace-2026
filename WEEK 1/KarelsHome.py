from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
   turn_three_times()
   move()
   turn_left()
   sprint()
   pick_beeper()
   turn_twice()
   sprint()
   turn_three_times()
   move()
   turn_three_times()


def turn_twice():
    turn_left()
    turn_left()

def turn_three_times():
    turn_left()
    turn_left()
    turn_left()

def sprint():
    move()
    move()
    move()




# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()