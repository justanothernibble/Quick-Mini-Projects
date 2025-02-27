print("Welcome to the shopping list")
def findItem(list, item):
    for i in range(len(list)):
        if  list[i] == item:
            return True
    return False

def remove(list, item):
    if findItem(list, item):
        list.remove(item)
    else:
        print("Item not found")

def view(list):
    for i in list:
        print(i)

def add(list, item):
    if not findItem(list, item):
        list.append(item)
    else:
        print("Item already exists")

def edit(list, item):
    if findItem(list, item):
        print("What would you like to change it to: ")
        try:
            change = str(input("> "))
        except Exception as e:
            print(f"Error: {e}")
        list[list.index(item)] = change
    else:
        print("Item not found")

print("Welcome to Shopping List")
list = []
while True:
    choice = int(input("What would you like to do?\n1. Add\n2.Edit\n3.Remove\n4. View\n5. Exit\n> "))
    if choice == 1:
        add(list, str(input("Enter the item you want to add\n> ")))
    elif choice == 2:
        edit(list, str(input("Enter the item you want to change\n> ")))
    elif choice == 3:
        remove(list, str(input("Enter the item you want to remove\n> ")))
    elif choice == 4:
        view(list)
        print("\n")
    elif choice == 5:
        break
    else:
        print("That is not an option")
    