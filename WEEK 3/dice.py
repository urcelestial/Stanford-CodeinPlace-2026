import random

def main():
    num = input("How many sides does your dice have?")
    num = int(num)
    roll = random.randint(1,num)
    print (f"Your roll is {roll}")


if __name__ == '__main__':
    main()