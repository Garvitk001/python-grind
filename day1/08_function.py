# FUNCTIONS - Industry Style



# ---- WHY FUNCTIONS? ----
# Bina function ke - repeat karna padta hai



def square(number):
    return number * number

print(square(2))
print(square(5))



# ---- FUNCTION KE 4 PARTS ----

#  1. def       = function banana shuru
#  2. name      = function ka naam
#  3. parameter = input jo function lega
#  4. return    = function kya wapas dega

print("="*40)
print("-------------EMI CALCULATOR-------------")
print("="*40)


"""
    EMI Calculator - Banks use karte hain
    loan_amount   : Total loan in rupees
    interest_rate : Annual interest rate (percentage)
    months        : Loan duration in months
    """

def calculate_emi(loan_amount,interest_rate,months):
    monthly_rate = interest_rate / (12*100)

    emi= loan_amount*monthly_rate * (1+monthly_rate)**months
    emi = emi / ((1 + monthly_rate)**months - 1)
    return round(emi,2)

emi = calculate_emi(500000, 8.5, 60)
print(f"Loan    : ₹5,00,000")
print(f"Rate    : 8.5% per year")
print(f"Period  : 60 months")
print(f"EMI     : ₹{emi:,}")