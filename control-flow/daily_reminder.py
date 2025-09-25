# daily_reminder_py38.py  (drop into the same path as daily_reminder.py)
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

if priority == "high":
    base = f"'{task}' is a high priority task"
elif priority == "medium":
    base = f"'{task}' is a medium priority task"
elif priority == "low":
    base = f"'{task}' is a low priority task"
else:
    base = f"'{task}' has an unknown priority. Please set high, medium, or low."

if time_bound == "yes":
    reminder = base + " that requires immediate attention today!"
else:
    reminder = base + ". Consider completing it when you have free time."

print("\nReminder:", reminder)

while True:
    if time_bound == "yes" and priority == "high":
        answer = input("\nHave you completed this high-priority task? (yes/no/stop): ").strip().lower()
    else:
        answer = input("\nMark as done? (yes/no/stop): ").strip().lower()

    if answer == "yes":
        print("\nNice! Well done on completing this task. Let the world hear about this milestone achieved. íº€")
        break
    elif answer == "no":
        print("\nReminder:", reminder)
    elif answer in ("stop", "snooze"):
        print("\nOkay â€” reminder snoozed. Run the script again when you're ready.")
        break
    else:
        print("Please answer 'yes', 'no', or 'stop'.")

