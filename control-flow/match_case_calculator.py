#!/usr/bin/env python3
# match_case_calculator.py
# Written for Python 3.8 / 3.9 (uses if-elif instead of match-case)

def get_number(prompt):
    """Prompt until the user enters a valid number. Returns a float."""
    while True:
        s = input(prompt)
        try:
            # Accept integers and floats; always convert to float for simplicity
            return float(s)
        except ValueError:
            print("Please enter a valid number.")  # user-friendly retry message

def main():
    # 1) Read the two numbers using the exact variable names requested
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    # 2) Ask for operation (exact prompt requested)
    op = input("Choose the operation (+, -, *, /): ").strip()

    # 3) Use if-elif to dispatch operations (works in Python 3.8/3.9)
    if op == '+':
        result = num1 + num2
        print(f"The result is {result}.")
    elif op == '-':
        result = num1 - num2
        print(f"The result is {result}.")
    elif op == '*':
        result = num1 * num2
        print(f"The result is {result}.")
    elif op == '/':
        # handle division by zero gracefully
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    else:
        print("Invalid operation chosen. Please choose one of +, -, *, /.")

if __name__ == "__main__":
    main()



