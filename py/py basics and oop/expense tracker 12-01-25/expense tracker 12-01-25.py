import os

# Set the default file directory to the one that the script is in
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print("Welcome to Expense Tracker!")
while True:
    print("What would you like to do?\n1. View Expenses\n2. Record Expense\n3. Exit")
    choice = int(input("> "))
    if choice == 1:
        try:
            with open("expenses.txt", "r") as f:
                lines = f.readlines()
                if not lines:
                    print("No expenses recorded yet")
                else:
                    for line in lines:
                        print(line.strip())
        except FileNotFoundError:
            print("No expenses recorded yet.")
    elif choice == 2:
        with open("expenses.txt", "a") as f:
            expense = input("What would you like to add? ")
            f.write(f"\n{expense}")
            print("Expense recorded.")
    elif choice == 3:
        print("Thanks for using.")
        break
    else:
        print("Invalid choice. Please try again.")