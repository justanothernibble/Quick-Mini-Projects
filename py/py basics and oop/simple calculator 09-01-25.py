"""
Edits that I would like to add in the future.
First of all, I would like to have dynamic typing.
This allows the user to avoid having to carefully put spaces everywhere, allowing a smoother experience.
Secondly, I would like to add more than 2 terms be possible.
This comes with the difficulty of assigning priority to exponents, then multiplication/division, then addition/subtraction.
"""
def evaluate(elist):

    for i in range(1, len(elist)): # We know that the first element is a number
        if elist[i] == "+":
            e1 = int(elist[i-1]) + int(elist[i+1])
            return e1
        elif elist[i] == "-":
            e1 = int(elist[i-1]) - int(elist[i+1])
            return e1
        elif elist[i] == "*":
            e1 = int(elist[i-1]) * int(elist[i+1])
            return e1
        elif elist[i] == "/":
            e1 = int(elist[i-1]) / int(elist[i+1])
            return e1
        elif elist[i] == "**":
            e1 = int(elist[i-1]) ** int(elist[i+1])
            return e1
        elif elist[i] == "%":
            e1 = int(elist[i-1]) % int(elist[i+1])
            return e1
        elif len(elist) == 1:
            return("You only entered 1 term")
            break
        else:
            return("I dont know.")
            

print("Welcome to Calculator")
while True:
    print("\nEnter your equation. Ensure all numbers are separated by a space")
    equation = input()
    elist = equation.split()
    print(elist)
    print("The result of your computation is: "+str(evaluate(elist)))
    print("Would you like to exit the calculator or compute again? Enter \"Exit\" to exit, and anything else to continue.")
    choice = str(input("> "))
    if choice == "Exit":
        break