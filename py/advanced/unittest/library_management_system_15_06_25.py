class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            raise Exception("Book is already checked out")
        self.is_checked_out = True

    def return_book(self):
        if not self.is_checked_out:
            raise Exception("Book is not checked out")
        self.is_checked_out = False
