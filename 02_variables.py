# 02_variables.py
# Variables store data. Python figures out the type automatically.
# Run: python 01_basics/02_variables.py

# --- DATA TYPES ---

# String (text) — wrapped in quotes
name = "Alice"
city = 'New York'

# Integer (whole number)
age = 25
score = 100

# Float (decimal number)
price = 9.99
pi = 3.14159

# Boolean (True or False — capital T/F!)
is_student = True
has_job = False

# --- PRINT THEM ---
print(name)         # Alice
print(age)          # 25
print(price)        # 9.99
print(is_student)   # True

# type() tells you what type a variable is
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(price))      # <class 'float'>
print(type(is_student)) # <class 'bool'>

# --- F-STRINGS (best way to print variables in text) ---
print(f"My name is {name} and I am {age} years old.")
print(f"Price: ${price}")
