
# ---- 1. ARITHMETIC OPERATORS ----
# Ye DS/ML mein calculations ke liye use hote hain



price = 1000
discount = 200
tax_rate = 0.18
quantity = 5

final_price = (price - discount)  * quantity
tax = final_price * tax_rate
total = final_price + tax

print(f"Price = {price}")
print(f"Discount = {discount}")
print(f"Tax Rate = {tax_rate}")
print(f"Quantity = {quantity}")
print(f"Final Price = {final_price}")
print(f"Tax 18% = {tax}")
print(f"Total = {total:,.2f}")




# ---- 2. COMPARISON OPERATORS ----
# Ye conditions mein use hote hain - ML mein filtering ke liye


age = 20 
salary =25000
cgpa = 7.8

print(f"\nAge 18 se bada hai? {age > 18}")
print(f"Salary 30000 se jada h?  {salary>30000}")
print(f"CGPA 8 se jada h?  {cgpa>8}")




# ---- 3. LOGICAL OPERATORS ----
# Ye sabse important hain - job eligibility, fraud detection, etc.

print(f"\n---------Job Eligibility Check---------")
print(f"Age and salary is ok? -- {age > 18  and salary>20000}")
print(f"Cgpa or experience? -- {cgpa>8 or True}")   
print(f"cgpa and exp? -- {cgpa>8 and True}")

print(f"blacklist check? -- {not False}")


# ---- 4. SPECIAL OPERATOR - jo 80% students nahi jaante ----
# % = modulus - remainder nikalta hai


number = 21

print(f"\n{number} is even or odd? ")
if number % 2 == 0:
        print(f"{number} is even.")
else:
        print(f"{number} is odd.")





# Real use - har 100vi row pe summary print karo

for i in range (1,1001):
        if i %100 == 0:
                print(f"Row {i} completed)")