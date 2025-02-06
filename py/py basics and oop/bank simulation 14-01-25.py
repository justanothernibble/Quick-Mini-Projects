"""
Bank account simulation
Two classes that interact with eachother
Bank class holds bank reserves. Only one object can exist for this class
Customer class holds account balance, which can deposit money into their bank account. 
+ When money is deposited, the bank gains 10% of the deposited amount in reserves.
+ When money is extracted, the bank loses 100% of the money.
"""

class Bank:
    def __init__(self, name, reserves):
        self.name = name
        self.reserves = reserves
    
    def takeCash(self, amount):
        self.reserves = self.reserves + amount
    
    def giveCash(self, amount):
        self.reserves = self.reserves - (amount/10)


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount, branch):
        self.balance = self.balance + amount
        branch.takeCash(amount)

    def withdraw(self, amount, branch):
        if self.balance >= amount:
            self.balance = self.balance - amount
            branch.giveCash(amount)
        else:
            print("Insufficient funds")
    
    def viewBalance(self):
        return self.balance
    
    def getName(self):
        return self.name

print("Before we start the simulation, we must create banks and accounts")
name = str(input("What would you like to call your bank?\n> "))
val = int(input("How much reserves would you like it to have?\n> "))
b1 = Bank(name, val)

name = str(input("What would you like to call your account?\n> "))
val = int(input("What initial balance would you like it to have?\n> "))
a1 = Account(name, val)


print(f"Welcome to Bank Account Simulation {a1.getName()}")
while True:
    try:
        choice = int(input("What would you like to do?\n1. Deposit\n2. Withdraw\n3. View Balance\n4. Exit\nEnter choice: "))
        if choice == 1: # deposit
            value = int(input("How much cash would you like to deposit?\n> "))
            a1.deposit(value, b1)
        elif choice == 2: # withdraw
            value = int(input("How much cash would you like to withdraw?\n> "))
            a1.withdraw(value, b1)
        elif choice == 3: # view balance
            print(f"Your balance is {a1.viewBalance()}")
        elif choice == 4: # exit application
            break
        else:
            print("That is not an option, choose again.")
    except Exception as e:
        print(f"An error occured: {e}")