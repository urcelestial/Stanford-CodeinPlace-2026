"""
1. Print prompt (prints every questions for every key
until there is none)
2. Cast input 
3. Prolly use an if statement for the answer
4. Print prompt correct/incorrect
5. Add scoring system

"""

def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    score = 0

    for word in translations:
        answer = input(f"What is the Spanish translation for {word}? ")

        correct = translations[word]

        if answer == correct:
            print("That is correct!")
            score = score + 1
        elif answer != correct:
            print(f"That is incorrect, the Spanish translation for {word} is {correct}.")

    print(f"You got {score}/8 words correct, come study again soon!")

        






if __name__ == '__main__':
    main()