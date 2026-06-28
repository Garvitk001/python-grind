customer_age = 25
customer_name = "Garvit"
customer_cgpa = 9.5
is_eligible = True
customer_salary =  352334.4535

print(f"Name = {customer_name} -> Type = {type(customer_name)}")
print(f"Age = {customer_age} -> Type = {type(customer_age)}")
print(f"CGPA = {customer_cgpa} -> Type = {type(customer_cgpa)}")
print(f"Eligible = {is_eligible} -> Type = {type(is_eligible)}")
print(f"Salary = {customer_salary:,.2f} -> Type = {type(customer_salary)}")




age_from_csv = "25"
salary_from_csv = "352334.4535"
active_from_csv = "1"

print(f"{type(age_from_csv)}")

print(age_from_csv + 5) 

age = int(age_from_csv)
salary = float(salary_from_csv)
is_active = bool(int(active_from_csv))

print(f"Age = {age} -> Type = {type(age)}")
print(f"Salary = {salary:,.2f} -> Type = {type(salary)}")
print(f"Active = {is_active} -> Type = {type(is_active)}")