import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7

    for i in range(1, max_attempts + 1):
        guessnumber = int(input("Try a number: "))

        if guessnumber < random_number:
            print("Too low!")
        elif guessnumber > random_number:
            print("Too high!")
        else:
            return " Congratulations, you win!"

    return f" Sorry, you're out of attempts. The number was {random_number}."

# Appel de la fonction
print(number_guessing_game())