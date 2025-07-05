# NUMMBER .GAME
import random

top_of_range = input("Type a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0 next time.")
        quit()
else:
    print("please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range) #bhere 10 is not included be uase if we want to include 10 w need to pass 11
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please type a number next time.")
        continue

    if user_guess == top_of_range:
        print("You got it!")
        break
    elif user_guess > top_of_range:
        print("You were above the number!")
    else:
        print("You were below the number!")
        

print("You got it in", guesses, "guesses")
