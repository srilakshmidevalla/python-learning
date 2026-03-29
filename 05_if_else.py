# 01_if_else.py
# Make decisions in code
# Run: python 02_control_flow/01_if_else.py

age = int(input("Enter your age: "))

# Basic if / elif / else
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# --- COMPARISON OPERATORS ---
# ==  equal to
# !=  not equal to
# >   greater than
# <   less than
# >=  greater than or equal
# <=  less than or equal

# --- LOGICAL OPERATORS ---
# and → both must be True
# or  → at least one must be True
# not → flips True/False

score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

passed = score >= 60
print(f"Score: {score} | Grade: {grade} | Passed: {passed}")

# Combining conditions
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Access granted!")
else:
    print("Access denied.")
