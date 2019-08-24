### Simple game where you have to guess a number ###
import random


def guess_game():
    range = int(input("Please enter how many numbers you would like to guess out of: "))
    roll = random.randint(1, range)
    guess = int(input("What is your guess?: "))
    while True:
        if guess > roll:
            print("Nope! too high.\n")
        elif guess < roll:
            print("Nope! too low.\n")
        else:
            print("Correct! good guessing.")
            break
        guess = int(input("What is your guess?: "))

guess_game()

