# 01_functions.py
# Functions = reusable blocks of code
# Run: python 03_functions/01_functions.py

# ---- DEFINE A FUNCTION ----
def greet():
    print("Hello! Welcome to Python.")

# Call it (as many times as you want)
greet()
greet()

# ---- PARAMETERS (inputs to function) ----
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")
greet_user("Bob")

# ---- RETURN VALUES ----
def add(a, b):
    return a + b            # Sends result back to caller

result = add(3, 5)
print(f"3 + 5 = {result}")

# ---- DEFAULT PARAMETERS ----
def power(base, exponent=2):    # exponent defaults to 2 if not provided
    return base ** exponent

print(power(4))         # 4² = 16
print(power(2, 10))     # 2¹⁰ = 1024

# ---- MULTIPLE RETURN VALUES ----
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([5, 2, 9, 1, 7])
print(f"Min: {low}, Max: {high}")

# ---- REAL EXAMPLE ----
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 1), category

bmi, cat = calculate_bmi(70, 1.75)
print(f"BMI: {bmi} → {cat}")
