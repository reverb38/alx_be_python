# daily_reminder.py

# Step 1: Prompt user for input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Step 2: Use match-case for priority handling (Python 3.10+)
match priority:
    case "high":
        base = f"'{task}' is a high priority task"
    case "medium":
        base = f"'{task}' is a medium priority task"
    case "low":
        base = f"'{task}' is a low priority task"
    case _:
        base = f"'{task}' has an unknown priority. Please set high, medium, or low."

# Step 3: Add time sensitivity
if time_bound == "yes":
    reminder = base + " that requires immediate attention today!"
else:
    reminder = base + ". Consider completing it when you have free time."

# Step 4: Print the reminder (strict format for checker)
print(f"Reminder: {reminder}")

# Step 5: Simple loop for repeated check-ins
while True:
    if time_bound == "yes" and priority == "high":
        answer = input("\nHave you completed this high-priority task? (yes/no/stop): ").strip().lower()
    else:
        answer = input("\nMark as done? (yes/no/stop): ").strip().lower()

    if answer == "yes":
        print("Nice! Well done on completing this task. Let the world hear about this milestone achieved.")
        break
    elif answer == "no":
        print(f"Reminder: {reminder}")
    elif answer in ("stop", "snooze"):
        print("Okay — reminder snoozed. Run the script again when you're ready.")
        break
    else:
        print("Please answer 'yes', 'no', or 'stop'.")

