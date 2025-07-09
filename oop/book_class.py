#!/usr/bin/python3
"""
Defines a Book class with magic methods for initialization,
string representation, and deletion.
"""

class Book:
    """
    Represents a book with title, author, and publication year.
    """

    def __init__(self, title, author, year):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Creating book {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an "official" string representation of the book,
        allowing to recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Prints a message when the Book object is deleted.
        """
        print(f"Deleting {self.title}")

if __name__ == "__main__":
    # Example usage (for testing the class independently)
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)
    print(repr(my_book))
    del my_book
