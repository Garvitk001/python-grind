# ============================================
# LOOPS - Industry Style
# Garvit - Day 1 - python-grind/day1/06_loops.py
# ============================================

# ---- 1. Basic for loop ----
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(f"Processing: {fruit}")


# ---- 2. range() wala loop ----

for i in range(1,11):
    print (i, end=" ")


# print even number
print(f"\nEven numbers from 2 to 30:\n ")
for i in range(2,30,2):
    print (i, end=" ") 


# 3. enumerate()

print("\n\n--- enumerate() ---")
students = ["Garvit", "Rahul", "Priya", "Amit"]

for index , name in enumerate(students,1):
    print(f"{index}. {name}")




# 4. while loop
# Jab pata nahi kitni baar loop chalega


print("\n\n--- while loop ---")
attempts= 0
max_attempts = 5

while attempts < max_attempts:
    attempts+=1
    print(f"Attempt {attempts} of {max_attempts}")
print(f"done")




# ---- 5. break aur continue ----
# Break - loop band kardo
# Continue - ye iteration skip karo



print("\n\n--- break aur continue ---")
for i in range(1, 11):
    if i == 6:
        print("6 mila - loop band!")
        break
    print(i, end=" ")

print("\n Continue example ")
for i in range (1,21):
    if i % 3 == 0:
        continue
    print(i, end=" ")