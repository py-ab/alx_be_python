#!/usr/bin/python3
"""
Demonstrates inheritance and composition with a library system.
"""

class Book:
    """
    Base class for representing a book.
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

    def __str__(self):
        """
        Returns a string representation of the book.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    """

    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance.

        Args:
            title (str): The title of the ebook.
            author (str): The author of the ebook.
            file_size (int): The file size of the ebook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the ebook,
        including the file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Represents a printed book, inheriting from Book.
    """

    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the print book,
        including the page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Represents a library that manages a collection of books.
    Demonstrates composition.
    """

    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book (Book): The Book, EBook, or PrintBook object to add.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book in the library.
        """
        for book in self.books:
            print(book)

if __name__ == "__main__":
    # Example usage (for testing the classes independently)
    my_library = Library()
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()
