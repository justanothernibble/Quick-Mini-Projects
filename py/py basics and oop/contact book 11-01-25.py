"""

    Add a Contact: Users can input a contact's name and phone number.
    View Contacts: Display all contacts in the contact book.
    Update a Contact: Modify an existing contact's phone number.
    Delete a Contact: Remove a contact from the book.
    Search for a Contact: Find a contact by name.

    Dictionary methods:

    clear()	Removes all items from the dictionary.
    copy()	Returns a shallow copy of the dictionary.
    fromkeys()	Creates a new dictionary from the given sequence of keys, with a specified value for each key.
    get(key)	Returns the value associated with the specified key; returns None if the key does not exist.
    items()	Returns a view object containing tuples of all key-value pairs in the dictionary.
    keys()	Returns a view object that displays a list of all keys in the dictionary.
    pop(key)	Removes and returns the value associated with the specified key; raises a KeyError if not found.
    popitem()	Removes and returns the last inserted key-value pair as a tuple.
    setdefault(key, default)	Returns the value of the specified key; if not present, inserts the key with the specified default value.
    update(other)	Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.
    values()	Returns a view object containing all values in the dictionary.

"""

cont = {}

print("Welcome to Contact Book")
while True:
    choice = int(input("What would you like to do?\n1. Add\n2. View\n3. Update\n4. Delete\n5. Search\n6. Exit\n> "))
    if choice == 1:
        name = str(input("Who do you want to add? \n> "))
        num = str(input("What is their number?\n> "))
        cont[name] = num
        print("Added successfully")
    elif choice == 2:
        for key, item in cont.items():
            print(f"{key}: {item}")
        print("")
    elif choice == 3:
        name = str(input("Who do you want to change? \n> "))
        num = str(input("What is their new number? \n> "))
        cont[name] = num
    elif choice == 4:
        name = str(input("Who do you want to delete? \n> "))
        try:
            cont.pop(name)
        except Exception as e:
            print(f"Error: {e}")
    elif choice == 5:
        name = str(input("Who's number do you want to see? \n> "))
        print(f"The number is: {cont[name]}")
    elif choice == 6:
        break
print("Thank you for using contact book")