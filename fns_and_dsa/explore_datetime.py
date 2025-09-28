from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format it as "YYYY-MM-DD HH:MM:SS"
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Get current date and time
    current_date = datetime.now()
    # Calculate future date
    future_date = current_date + timedelta(days=days)
    # Format it as "YYYY-MM-DD"
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Ask user for number of days and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

