# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    num = input("Enter an age in calendar years: ")
    num = int(num)
    total = DOG_YEARS_MULTIPLIER * num
    print(f"That's {total} in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()