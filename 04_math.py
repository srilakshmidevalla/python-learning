# 04_math.py
# Python as a calculator
# Run: python 01_basics/04_math.py

a = 10
b = 3

print(a + b)    # Addition       → 13
print(a - b)    # Subtraction    → 7
print(a * b)    # Multiplication → 30
print(a / b)    # Division       → 3.333... (always float)
print(a // b)   # Floor division → 3 (drops remainder)
print(a % b)    # Modulo         → 1 (remainder only)
print(a ** b)   # Exponent       → 1000 (10 to the power of 3)

# Order of operations: same as math (PEMDAS)
result = 2 + 3 * 4      # → 14, not 20
result2 = (2 + 3) * 4   # → 20 (brackets first)
print(result, result2)

# Useful built-in functions
print(abs(-7))          # Absolute value → 7
print(round(3.7))       # Round → 4
print(round(3.14159, 2))# Round to 2 decimals → 3.14
print(max(5, 2, 9, 1))  # Largest → 9
print(min(5, 2, 9, 1))  # Smallest → 1

# Real example: tip calculator
bill = 50.0
tip_percent = 18
tip = bill * (tip_percent / 100)
total = bill + tip
print(f"Bill: ${bill} | Tip: ${tip:.2f} | Total: ${total:.2f}")
