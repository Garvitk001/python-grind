# ============================================
# CONDITIONS - Industry Style
# Garvit - Day 1 - python-grind/day1/04_conditions.py
# ============================================






age = 20

if age > 18:
    print(f"Adult")
elif age >13:
    print(f"Teenager")
else:
    print(f"Child")







# ============================================
# REAL INDUSTRY USE - Loan Eligibility System
# ============================================



def check_loan_eligibility(name,age,salary,credit_score):
    
    print(f"\n---Loan Eligibility Check {name}---")

    #condition 1 age check
    if age <21 or age > 60:
        print(f" REJECTED - Age eligible nahi hai (21-60 chahiye)")
        return
    
    if salary < 25000:
        print(f" REJECTED - Salary eligible nahi hai (25k+ chahiye)")
        return
    
    if credit_score < 650:
        print(f" REJECTED - Credit Score eligible nahi hai (700+ chahiye)")
        return
    
    #Loan Amount decided based on salary and credit score
    
    if salary >50000 and credit_score >800:
        loan_amount = salary * 20
        category = "Premium"

    elif salary > 40000 and credit_score >700:
        loan_amount = salary * 15
        category = "Gold"
 
    else:
        loan_amount = salary * 10
        category = "Silver"


    print(f"Approved -  {category} Category)")
    print(f"Max loan amount = {loan_amount}")


check_loan_eligibility("Garvit",  25, 45000, 720)
check_loan_eligibility("Rahul",   19, 45000, 720)
check_loan_eligibility("Priya",   30, 20000, 720)
check_loan_eligibility("Amit",    35, 80000, 850)