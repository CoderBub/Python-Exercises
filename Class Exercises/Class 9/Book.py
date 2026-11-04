class Book:
    def __init__(self, title):
        self.title = title
        self.checked_out = False

class Member:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def checkout(self, title):
        for book in self.books:
            if book.title == title and not book.checked_out:
                book.checked_out = True
                print(f"{title} checked out")
                return
        print("Book not available")

library = Library()
library.add_book(Book("1984"))
library.checkout("1984")
