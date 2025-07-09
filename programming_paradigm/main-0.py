#!/usr/bin/python3
"""
A script to interact with the BankAccount class via command line arguments.
"""

import sys
from bank_account import BankAccount

def main():
    """
    Main function to process command line arguments and interact with the BankAccount class.
    """
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command, *params = sys.argv[1].split(':')
        amount_str = params[0] if params else None  # get amount as a string
        amount = float(amount_str) if amount_str is not None else None
    except ValueError:
        print("Invalid amount. Please provide a numeric value.")
        sys.exit(1)


    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
