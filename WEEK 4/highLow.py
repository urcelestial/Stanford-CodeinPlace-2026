import random


"""
MILESTONE 1
1. Configure a random number for both the coputer and the user
using the random.randint command
"""
NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    comp_num = random.randint(1,100)
    my_num = random.randint(1,100)

    print(f"The computer's number is {comp_num}")
    print(f"Your number is {my_num}")

"""
MILESTONE 2
2. Cast an input where the user gets to choose whether their number
is higher or lower than the computers'
"""
def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    comp_num = random.randint(1,100)
    my_num = random.randint(1,100)

    print(f"The computer's number is {comp_num}")
    print(f"Your number is {my_num}")

    choose = input("Do you think your number is higher or lower than the computer's?: ")

"""
MILESTONE 3
3. Write the game logic 
4. Give out the output whether the answer is correct or not
"""

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    comp_num = random.randint(1,100)
    my_num = random.randint(1,100)

    print(f"The computer's number is {comp_num}")
    print(f"Your number is {my_num}")

    choose = input("Do you think your number is higher or lower than the computer's?: ")

    lower = my_num < comp_num
    higher = my_num > comp_num

    if choose == "lower" and lower == True:
        print(f"You were right! The computer's number was {comp_num}")
    elif choose == "lower" and lower == False:
        print(f"Aww, that's incorrect. The computer's number was {comp_num}")
    elif choose == "higher" and higher == True:
        print(f"You were right! The computer's number was {comp_num}")
    elif choose == "higher" and higher == False:
        print(f"Aww, that's incorrect. The computer's number was {comp_num}")

"""
MILESTONE 4
5. Change the game into 5 round (repeated rounds)
"""
def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    game_round = 1

    for i in range (NUM_ROUNDS):
        print(f"Round {game_round}")

        comp_num = random.randint(1,100)
        my_num = random.randint(1,100)

        print(f"Your number is {my_num}")

        choose = input("Do you think your number is higher or lower than the computer's?: ")

        lower = my_num < comp_num
        higher = my_num > comp_num

        if choose == "lower" and lower == True:
            print(f"You were right! The computer's number was {comp_num}")
        elif choose == "lower" and lower == False:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")
        elif choose == "higher" and higher == True:
            print(f"You were right! The computer's number was {comp_num}")
        elif choose == "higher" and higher == False:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")

        game_round = game_round + 1

"""
MILESTONE 5
6. Add a scoring system
7. Add a final prompt when the game ends
"""

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    game_round = 1
    score = 0

    for i in range (NUM_ROUNDS):
        print(f"Round {game_round}")

        comp_num = random.randint(1,100)
        my_num = random.randint(1,100)

        print(f"Your number is {my_num}")

        choose = input("Do you think your number is higher or lower than the computer's?: ")

        lower = my_num < comp_num
        higher = my_num > comp_num

        if choose == "lower" and lower == True:
            print(f"You were right! The computer's number was {comp_num}")
            score = score + 1
        elif choose == "lower" and lower == False:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")
        elif choose == "higher" and higher == True:
            print(f"You were right! The computer's number was {comp_num}")
            score = score + 1
        elif choose == "higher" and higher == False:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")

        print(f"Your score is now {score}")

        game_round = game_round + 1

    print("Thanks for playing!")


if __name__ == "__main__":
    main()