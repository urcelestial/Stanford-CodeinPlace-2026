import random

num1 = (random.randint(10,99))
num2 = (random.randint(10,99))

def main():

    print("Khansole Academy")

    print(f"What is {num1} + {num2}?")
    answer = input("Your answer: ")
    answer = int(answer)

    correct_answer = num1 + num2

    if answer == correct_answer :
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {correct_answer}")

    
    
if __name__ == '__main__':
    main()