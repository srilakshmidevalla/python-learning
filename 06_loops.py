# 02_loops.py
# Repeat code automatically
# Run: python 02_control_flow/02_loops.py

# ---- FOR LOOP ----
# Use when you know how many times to repeat

# Loop through a range of numbers
for i in range(5):          # 0, 1, 2, 3, 4
    print(f"Count: {i}")

# range(start, stop, step)
for i in range(1, 11, 2):   # 1, 3, 5, 7, 9
    print(i, end=" ")
print()  # newline

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop through a string
for letter in "Python":
    print(letter, end="-")
print()

# ---- WHILE LOOP ----
# Use when you don't know how many times in advance

countdown = 5
while countdown > 0:
    print(f"Launching in {countdown}...")
    countdown -= 1         # Same as: countdown = countdown - 1
print("🚀 Liftoff!")

# Infinite loop with break (careful!)
while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break              # Exit the loop immediately
    print(f"You typed: {answer}")

# --- LOOP CONTROL ---
# break    → exit loop completely
# continue → skip to next iteration
# pass     → do nothing (placeholder)

for i in range(10):
    if i == 3:
        continue           # Skip 3
    if i == 7:
        break              # Stop at 7
    print(i, end=" ")
print()
