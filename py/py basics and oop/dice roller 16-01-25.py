"""Day 10: Python Libraries (Importing and Using Libraries)
Topics: Importing and using libraries (math, random).

Key Concepts to Cover:

    Understanding how to import libraries (import, from ... import).
    Using built-in Python libraries like math (for mathematical operations) and random (for generating random values).
    Exploring functions in the math module like math.sqrt(), math.factorial(), math.pi, etc.
    Using random.randint(), random.choice(), random.shuffle(), etc., from the random module.

Mini-project: Dice Roller

This mini-project involves simulating the roll of dice. The user should be able to roll a dice with any number of sides (e.g., 6-sided, 20-sided), and the program should return a random result from that range.

Steps:

    Create a function to roll a dice with a given number of sides.
    Use the random module to generate random numbers between 1 and the number of sides.
    Allow the user to input the number of sides for the dice (e.g., 6 for a standard dice or 20 for a D20).
    Optionally, ask the user if they want to roll again.
"""
from random import randint
def roll(sides):
    return randint(1, sides)

print("Welcome to dice roller")
while True:
    choice = int(input("Would you like to... 1. roll again or 2. quit\n> "))
    if choice == 1:
        sides = int(input("How many sides?\n> "))
        print(roll(sides))
    elif choice == 2:
        break
    else:
        print("that is not an option")