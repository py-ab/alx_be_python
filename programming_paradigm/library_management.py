#!/usr/bin/python3
"""
Implementation of a basic Library Management System using OOP.
"""

class Book:
    """
    Represents a book with a title, author, and availability status.
    """

    def __init__(self, title, author):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially available

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned (available).
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is currently available.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the book.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Represents a library that manages a collection of books.
    """

    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book (Book): The Book object to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book from the library by title.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return  # Book checked out, exit the loop
        # If the book is not found or not available, do nothing

    def return_book(self, title):
        """
        Returns a book to the library by title.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return  # Book returned, exit the loop
        # If the book is not found or already available, do nothing

    def list_available_books(self):
        """
        Lists the available books in the library.
        """
        for book in self._books:
            if book.is_available():
                print(book)

if __name__ == "__main__":
    # Example usage (for testing the classes independently)
    library = Library()
    book1 = Book("Brave New World", "Aldous Huxley")
    book2 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)

    print("Available books after setup:")
    library.list_available_books()

    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
