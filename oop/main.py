#!/usr/bin/python3
"""
Test script for the Book class, demonstrating the use of
magic methods.
"""

from book_class import Book

def main():
    """
    Main function to demonstrate Book class functionality.
    """
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the str method
    print(my_book)  # Expected to use str

    # Demonstrating the repr method
    print(repr(my_book))  # Expected to use repr

    # Deleting a book instance to trigger del
    del my_book

if __name__ == "__main__":
    main()
