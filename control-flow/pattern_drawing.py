#!/usr/bin/python3

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using a while loop and a for loop
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line
    row += 1

