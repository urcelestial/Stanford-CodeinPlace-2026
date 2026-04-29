from karel.stanfordkarel import *

def main():
    while beepers_present():
        move()
        follow_beepers()

def follow_beepers():
    if no_beepers_present():
        celebrate()
    else:
        move()

def celebrate():
    for i in range (4):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()