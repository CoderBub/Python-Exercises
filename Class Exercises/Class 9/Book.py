#
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def checkout(self, title):
        for book in self.books:
            if book.title == title and not book.checked_out:
                book.checked_out = True
                print(f"{book.title} by {book.author} checked out")
                return
        print("Book not available")

library = Library()
library.add_book(Book("1984", "Orwell"))
library.checkout("1984")
library.add_book(Book("Animal Farm", "Orwell"))

library.checkout("Animal Farm")

