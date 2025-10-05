# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats (handles numeric strings too)
        num = float(numerator)
        den = float(denominator)

        # Handle division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform the division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handles cases like 'ten' or other non-numeric inputs
        return "Error: Please enter numeric values only."

