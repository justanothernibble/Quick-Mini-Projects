"""
Library Management System
Firstly I must make a library class. 
This will interact with person objects
    ...that will aggregate book objects 
        which will have attributes name, ISBN, author


"""

class Member():
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.current_books = []
        self.book_count = 0
    
    def borrow_book(self, isbn, lib):
        temp = None
        found = False
        if self.book_count == self.max_borrow_limit:
            print("You have borrowed too many books. Return one and come back later.")
        else:
            for i in range(len(lib.books)):
                if lib.books[i].isbn == isbn:
                    temp = lib.books[i]
                    found = True
                    break
        if found == False and not (self.book_count == self.max_borrow_limit):
            print("Book not found. Try another ISBN")
        elif not self.book_count == self.max_borrow_limit:
            self.book_count +=1
            lib.remove_book(temp)
            temp.status = "Borrowed"
            self.current_books.append(temp)
            print(f"Book: {temp.title} has been borrowed and added to your list of current books.")
        else:
            pass
        

    def view_books(self):
        for i in range(len(self.current_books)):
            print(f"{i+1}: {self.current_books[i].title}, written by: {self.current_books[i].author}. ISBN: {self.current_books[i].isbn}")



    def return_book(self, isbn, lib): # takes the isbn of the book and library
        temp = None
        found = False
        for i in range(len(self.current_books)):
            if self.current_books[i].isbn == isbn:
                temp = self.current_books[i]
                found = True
                break
        if found == False:
            print("Book not found. Try another ISBN")
        else:
            self.book_count -= 1
            self.current_books.remove(temp)
            temp.status = "Returned"
            print(f"Book: {temp.title} has been borrowed and removed from your list of current books.")
            lib.add_book(temp)


class Teacher(Member):
    def __init__(self, name, member_id, department):
        super().__init__(name, member_id)
        self.department = department
        self.max_borrow_limit = 2

class Student(Member):
    def __init__(self, name, member_id, grade):
        super().__init__(name, member_id)
        self.grade = grade
        self.max_borrow_limit = 1

class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self, b1): # this occurs when a book is returned from person
        self.books.append(b1)
        print(f"Book: {b1.title} has been added to library successfully")

    def remove_book(self, b1):
        try:
            self.books.remove(b1)
        except Exception as e:
            print(f"Book not available. Choose a different IBSN. \n(Error: {e})")
    
    def view_lib(self):
        for i in range(len(self.books)):
            print(f"{i+1}: {self.books[i].title}, written by: {self.books[i].author}. ISBN: {self.books[i].isbn}")

class Book():
    def __init__(self, title, author, isbn, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

l1 = Library()
l1.books.extend([
    Book("Meditations", "Marcus Aurelius", "436", "Returned"),
    Book("Bible", "???", "145", "Returned"),
    Book("1984", "George Orwell", "984", "Returned"),
    Book("10 Commandments", "Moses of Egypt", "100", "Returned"),
    Book("Calc 1", "Math Wiz", "582", "Returned")
])


choice = input("Student or Teacher? Input s/t\n> ")
na = input("What is your name?\n> ")
id = input("What is your member ID?\n> ")
m1 = None
if choice == "s":
    gra = input("What is your grade?\n> ")
    m1 = Student(na, id, gra)
elif choice == "t":
    dept = input("What is your department?\n> ")
    m1 = Teacher(na, id, dept)
while True:
    choice = int(input(f"\nGreetings {m1.name}, welcome to the Library.\nWhat would you like to do?\n1. Borrow a book\n2. Return a book\n3. View inventory\n4. View currently held books\n5. Exit\n> "))
    if choice == 1: # borrow
        isbn = input("Enter the ISBN of the book you want to borrow\n> ")
        m1.borrow_book(isbn, l1)
    elif choice == 2: # return
        isbn = input("Enter the ISBN of the book you want to return\n> ")
        m1.return_book(isbn, l1)
    elif choice == 3: # view inventory
        l1.view_lib()
    elif choice == 4: # view available
        m1.view_books()
    elif choice == 5: # exit
        print("Thank you for using the application")
        break
    else:
        print("That is not an option!")