# 02_dictionaries.py
# Dictionaries: key → value pairs (like a real dictionary)
# Run: python 04_data_structures/02_dictionaries.py

# ---- CREATE ----
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}

# ---- ACCESS ----
print(person["name"])               # Alice
print(person.get("age"))            # 30
print(person.get("salary", 0))      # 0 (default if key missing — safe!)

# ---- MODIFY ----
person["age"] = 31                  # Update existing
person["email"] = "alice@email.com" # Add new key
del person["is_student"]            # Delete key

# ---- LOOP ----
for key in person:
    print(key)                      # Keys only

for key, value in person.items():
    print(f"{key}: {value}")        # Keys + values

print(list(person.keys()))          # All keys as list
print(list(person.values()))        # All values as list

# ---- CHECK KEY EXISTS ----
if "email" in person:
    print(f"Email: {person['email']}")

# ---- NESTED DICT (dict inside dict) ----
students = {
    "s001": {"name": "Bob", "grade": "A", "score": 95},
    "s002": {"name": "Carol", "grade": "B", "score": 82},
}

for student_id, info in students.items():
    print(f"{student_id}: {info['name']} → {info['grade']}")

# ---- PRACTICAL: word counter ----
sentence = "the cat sat on the mat the cat"
word_count = {}

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
