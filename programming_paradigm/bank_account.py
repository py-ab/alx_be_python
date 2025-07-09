#!/usr/bin/python3
"""
A simple BankAccount class.
"""

class BankAccount:
    """
    Represents a bank account with deposit, withdraw, and display balance functionality.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an initial balance.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount > 0:
            self.__account_balance += amount
        #No need to print here. main-0.py should handle the printing

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.
        Returns True if withdrawal is successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False  # Important:  Return False if withdrawal fails

    def display_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance}")
