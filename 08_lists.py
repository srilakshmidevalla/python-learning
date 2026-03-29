# 01_lists.py
# Lists: ordered, changeable collection
# Run: python 04_data_structures/01_lists.py

# ---- CREATE ----
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", True, 3.14]   # Can mix types

# ---- ACCESS ----
print(fruits[0])        # apple  (index starts at 0)
print(fruits[-1])       # cherry (last item)
print(fruits[1:3])      # ['banana', 'cherry'] (slice)

# ---- MODIFY ----
fruits.append("mango")         # Add to end
fruits.insert(1, "blueberry")  # Add at index 1
fruits.remove("banana")        # Remove by value
popped = fruits.pop()          # Remove & return last item
fruits[0] = "avocado"          # Change item

# ---- LOOP ----
for fruit in fruits:
    print(fruit)

# Loop with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# ---- USEFUL METHODS ----
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(nums))            # Length → 8
print(sorted(nums))         # Sorted copy → [1, 1, 2, 3, 4, 5, 6, 9]
print(sum(nums))            # Sum → 31
print(nums.count(1))        # Count of 1 → 2
print(1 in nums)            # Check membership → True

# ---- LIST COMPREHENSION (power feature) ----
squares = [x**2 for x in range(1, 6)]
print(squares)              # [1, 4, 9, 16, 25]

evens = [x for x in range(20) if x % 2 == 0]
print(evens)                # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
