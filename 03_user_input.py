# 03_user_input.py
# input() pauses the program and waits for the user to type something.
# Run: python 01_basics/03_user_input.py

# Basic input — always returns a STRING
name = input("What is your name? ")
print(f"Hello, {name}!")

# Converting input to a number
age_str = input("How old are you? ")
age = int(age_str)          # int() converts string → integer
print(f"Next year you'll be {age + 1}!")

# Shortcut: convert directly
height = float(input("Your height in meters? "))
print(f"Your height: {height}m")

# Common mistake: forgetting to convert input
# WRONG:  print(age + 5)       ← if age is still a string, this crashes
# RIGHT:  print(int(age) + 5)
