# 01_file_handling.py
# Read and write files
# Run: python 05_file_handling/01_file_handling.py

import os

# ---- WRITE A FILE ----
with open("05_file_handling/output_demo.txt", "w") as f:
    f.write("Hello, File!\n")
    f.write("This is line 2.\n")
    f.write("Python file handling is easy.\n")

print("File written!")

# ---- READ ENTIRE FILE ----
with open("05_file_handling/output_demo.txt", "r") as f:
    content = f.read()
print("Full content:")
print(content)

# ---- READ LINE BY LINE ----
with open("05_file_handling/output_demo.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"Line {i}: {line.strip()}")  # .strip() removes \n

# ---- APPEND TO FILE (don't overwrite) ----
with open("05_file_handling/output_demo.txt", "a") as f:
    f.write("This line was appended!\n")

# ---- READ LINES INTO A LIST ----
with open("05_file_handling/output_demo.txt", "r") as f:
    lines = f.readlines()   # Returns list of strings

print(f"Total lines: {len(lines)}")

# ---- CHECK IF FILE EXISTS ----
if os.path.exists("05_file_handling/output_demo.txt"):
    print("File exists!")
    size = os.path.getsize("05_file_handling/output_demo.txt")
    print(f"File size: {size} bytes")

# ---- MINI PROJECT: Simple Diary ----
def add_entry(entry):
    with open("05_file_handling/my_diary.txt", "a") as f:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"[{timestamp}] {entry}\n")

def read_diary():
    try:
        with open("05_file_handling/my_diary.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No entries yet."

add_entry("Started learning Python today!")
add_entry("File handling is pretty cool.")
print("\n--- Diary ---")
print(read_diary())
