from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 26 beepers, and end facing East to 
the right of the 26 beepers.
"""

def main():
# Putting 20 beepers in the first spot
    for i in range(20):
        put_beeper()
# Move forward once
    move()
# Putting 26 beepers in the second spot
    for i in range(26):
        put_beeper()
# Move forward once again
    move()

if __name__ == '__main__':
    main()