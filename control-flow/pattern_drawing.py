# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to go through rows
while row < size:
    # For loop to print each column of the row
    for col in range(size):
        print("*", end="")
    # Move to the next line after one row is printed
    print()
    # Increase row count
    row += 1

