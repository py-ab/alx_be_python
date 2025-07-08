#!/usr/bin/python3

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        priority_message = "a high priority task"
    case "medium":
        priority_message = "a medium priority task"
    case "low":
        priority_message = "a low priority task"
    case _:
        priority_message = "a task with unspecified priority"

# Modify reminder if the task is time-bound
if time_bound.lower() == "yes":
    time_message = " that requires immediate attention today!"
elif time_bound.lower() == "no":
    if priority == "low":
      time_message = ". Consider completing it when you have free time."
    else:
      time_message = ". Do not forget about it!"
else:
    time_message = "" # added in case user enters wrong input for time_bound

# Provide a customized reminder
if priority == "low" and time_bound.lower() == "no":
    print(f"Note: '{task}' is a {priority_message}{time_message}")
else:
    print(f"Reminder: '{task}' is {priority_message}{time_message}")

# Tweet Link
print("Well done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")
