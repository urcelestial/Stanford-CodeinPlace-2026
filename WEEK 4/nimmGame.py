"""
MILESTONE 1:
    1. Set variable stones = 20
    (possible into a 'i')
    2. create first prompt
    3. create second prompt
    4. cast an input for the second prompt 
    5. convert it into an integer
    6. it repeats the question and prompt
    7. when it ends, the game prints the last prompt

"""


def main():
    stones = 20 #Starting with 20 stones
    while stones > 0: #As long as the stones are more than zero, the game continues and repeats the process
        print(f"There are {stones} stones left.")
        num = input("Would you like to remove 1 or 2 stones? ")
        num = int(num)
        stones = stones - num #Whatever amount of stones there was, is subtracted by the number that user inputs
    print("Game over") #When there are no stones left, the game is over

"""
MILESTONE 2:
    1. add player 1 and player 2
    2. they take turns

"""

def main():
    stones = 20 #Starting with 20 stones
    player = 1 #Starting with Player 1

    while stones > 0: #As long as the stones are more than zero, the game continues and repeats the process
        print(f"There are {stones} stones left.")

        num = input(f"Player {player} would you like to remove 1 or 2 stones? ")
        num = int(num)

        stones = stones - num #Whatever amount of stones there was, is subtracted by the number that user inputs

        if player == 1: 
            player = player + 1 #If the player is currently player 1, then player 2 will take turn on the loop 
        else:
            player = player - 1 #If the player is currently player 2, then player 1 will take turn on the loop 

    print("Game over") #When there are no stones left, the game is over

"""
MILESTONE 3:
    Do not let the players enter a number greater than 2
"""

def main():
    stones = 20 #Starting with 20 stones
    player = 1 #Starting with Player 1

    while stones > 0: #As long as the stones are more than zero, the game continues and repeats the process
        print(f"There are {stones} stones left.")

        num = input(f"Player {player} would you like to remove 1 or 2 stones? ")
        num = int(num)

        input_is_invalid = True #The player did not enter an appropriate number
        while input_is_invalid :
            num = input("Please enter 1 or 2: ") #The player will be asked to put a number again until it follows the rules
            num = int(num)
            if num == 1 or num == 2:
                input_is_invalid = False #If the player enters the number accordingly, the loop stops and continue to the next step

        num = int(num)
        stones = stones - num #Whatever amount of stones there was, is subtracted by the number that user inputs


        if player == 1: 
            player = player + 1 #If the player is currently player 1, then player 2 will take turn on the loop 
        else:
            player = player - 1 #If the player is currently player 2, then player 1 will take turn on the loop 

    print("Game over") #When there are no stones left, the game is over

"""
MILESTONE 4:
    if a player ends up taking the rest of the stones, the other player wins
"""

def main():
    stones = 20 #Starting with 20 stones
    next_player = 1 #Starting with Player 1

    while stones > 0: #As long as the stones are more than zero, the game continues and repeats the process
        print(f"There are {stones} stones left.")

        num = input(f"Player {next_player} would you like to remove 1 or 2 stones? ")
        num = int(num)

        input_is_invalid = True #The player did not enter an appropriate number
        while input_is_invalid :
            num = input("Please enter 1 or 2: ") #The player will be asked to put a number again until it follows the rules
            num = int(num)
            if num == 1 or num == 2:
                input_is_invalid = False #If the player enters the number accordingly, the loop stops and continue to the next step

        num = int(num)
        stones = stones - num #Whatever amount of stones there was, is subtracted by the number that user inputs


        if next_player == 1:
            next_player = next_player + 1 #If the player is currently player 1, then player 2 will take turn on the loop 
        else:
            next_player = next_player - 1 #If the player is currently player 2, then player 1 will take turn on the loop 

    if next_player == 1:
        print("Player 1 wins!") #If the next player is Player 1 but the stones are already out, then Player 1 is the winner
    else:
        print("Player 2 wins!") #If the next player is Player 2 but the stones are already out, then Player 2 is the winner

if __name__ == '__main__':
    main()