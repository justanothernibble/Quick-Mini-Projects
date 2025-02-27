from random import randint

print("Welcome to Number guessing game")
while True:
    flag = True
    life = 3
    num = randint(1,10)
    print("Choose a random number from 1 to 10")
    while flag == True:
        guess = int(input("Enter your guess: "))
        if guess == num:
            print("Correct! 10 Billion points")
            break
        elif guess != num:
            life=life-1
            if life > -1:
                print(f"Wrong! you have {life} lives left")
            if life == -1:
                print("Game Over")
                flag = False
    print("Would you like to play again? Enter Y for yes, and N for no.")
    play = input()
    if play == "N":
        break

print("Thanks for playing")