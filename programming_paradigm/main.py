#!/usr/bin/python3
"""
Main script to interact with safe_divide function via command line arguments.
"""

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to process command line arguments and perform division.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()

