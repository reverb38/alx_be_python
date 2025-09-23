#!/usr/bin/env python3
# match_case_calculator.py
# Written for Python 3.8 / 3.9 (uses if-elif instead of match-case)

def get_number(prompt):
        """Prompt until the user enters a valid number. Returns a float."""
            while True:
                        s = input(prompt)
                                try:
                                                return float(s)
                                                    except ValueError:
                                                                    print("Please enter a valid number.")

                                                                    def main():
                                                                            num1 = get_number("Enter the first number: ")
                                                                                num2 = get_number("Enter the second number: ")
                                                                                    op = input("Choose the operation (+, -, *, /): ").strip()

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
                                                                                                                                                                            if num2 == 0:
                                                                                                                                                                                            print("Cannot divide by zero.")
                                                                                                                                                                                                    else:
                                                                                                                                                                                                                    result = num1 / num2
                                                                                                                                                                                                                                print(f"The result is {result}.")
                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                print("Invalid operation chosen. Please choose one of +, -, *, /.")

                                                                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                                                                        main()

