import os

# Set the default file directory to the one that the script is in
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def remove_element(lst, value):
    # Check if the value exists in the list
    if value not in lst:
        raise ValueError(f"{value} not found in list")
    
    for i in range(len(lst)):
        if lst[i] == value:
            # Remove the element by shifting elements to the left
            for j in range(i, len(lst) - 1):
                lst[j] = lst[j + 1]
            lst.pop()  # Remove the last element after shifting
            return  # Exit after removing the first occurrence of the value

def add(item):
    f = open("tasks.txt", "a")
    f.write(f"\n{item}")
    f.close()

def view():
    f = open("tasks.txt", "r")
    while True:
        if f.readline() == "":
            break
        print(f"\n{f.readline()}")
    f.close()
        
def remove(item):
    f = open("tasks.txt", "r")
    lines = f.readlines()
    for i in range(len(lines)):
        if lines[i] == item:
            remove_element(lines, item)
            break
    f.close()
    f = open("tasks.txt", "w")
    f.writelines(lines)
    f.close()

while True:
    try: 
        choice = int(input("Welcome to Task Management system. \nWhat would you like to do?\n1. Add\n2. View\n3. Remove\n4. Exit\n> "))
        if choice == 1:
            item = str(input("What would you like to add?\n> "))
            add(item)
        if choice == 2:
            view()
        if choice == 3:
            item = str(input("What would you like to remove?"))
            remove(item)
        if choice == 4:
            break
    except Exception as e:
        print(f"Error: {e}")