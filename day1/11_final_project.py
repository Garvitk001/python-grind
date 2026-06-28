# ============================================
# STUDENT RESULT MANAGEMENT SYSTEM
# ============================================






students = [
    {"name": "Garvit Khuteta",  "marks": [85, 92, 78, 90, 88]},
    {"name": "Rahul Sharma",  "marks": [65, 70, 58, 72, 68]},
    {"name": "Priya Singh",   "marks": [92, 95, 98, 91, 96]},
    {"name": "Amit Verma",    "marks": [45, 52, 48, 55, 50]},
    {"name": "Deepak Gupta",  "marks": [75, 80, 72, 85, 78]},
]

subjects = ["Math", "Science", "English", "Hindi", "Computer"]


def calculate_average(marks):
    total_marks = sum(marks)
    average= total_marks/len(marks)
    return round(average, 2)
    

def get_grade(average):
    if average >= 90:
        return "A+"
        
    elif average >= 80:
        return "A"
    
    elif average >= 70:
        return "B"
    elif average>= 60:
        return "C"
        return
    elif average>= 50:
        return "D"
    else :
        return "F"
       
    

def get_status(average):
    if average <51:
        return "FAIL"
    else:
        return "PASS"
    


# Test karo functions
# Test karo functions
print(calculate_average([85, 92, 78, 90, 88]))  # 86.6
print(get_grade(86.6))                           # A
print(get_status(86.6))                          # PASS
print(get_status(45.0))                          # FAIL               # FAIL









# ============================================
# FINAL REPORT - Sab functions use honge yahan
# ============================================

print("=" * 55)
print("         STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 55)
print(f"{'#':<4} {'Name':<18} {'Avg':<8} {'Grade':<8} {'Status'}")
print("-" * 55)

topper = ""
topper_avg = 0
fail_count = 0

for index, student in enumerate(students, 1):
    name    = student["name"]
    marks   = student["marks"]
    avg     = calculate_average(marks)
    grade   = get_grade(avg)
    status  = get_status(avg)

    # Topper track karo
    if avg > topper_avg:
        topper_avg = avg
        topper = name

    # Fail count karo
    if status == "FAIL":
        fail_count += 1

    print(f"{index:<4} {name:<18} {avg:<8} {grade:<8} {status}")

print("=" * 55)
print(f" Topper      : {topper} ({topper_avg}%)")
print(f" Failed      : {fail_count} students")
print(f" Class Avg   : {calculate_average([calculate_average(s['marks']) for s in students])}%")
print("=" * 55)