def calculate_average(number):
    return round(sum(number) / len(number),2)

def get_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    else: return "F"

def clean_name(name):
    return name.strip().title()

def is_valid_cgpa(cgpa):
    return 0.0 <= cgpa <= 10.0

def format_currency(amount):
    return f"₹{amount:,.2f}"