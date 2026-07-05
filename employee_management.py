import utils
import csv
from datetime import datetime

class Employee:
    def __init__(self, emp_id, name, dept, salary, joining_date):
        self.emp_id = emp_id
        self.name = utils.clean_name(name)
        self.dept = dept
        self.salary = salary
        self.joining_date = joining_date

    def get_info(self):
        print(f"\n{'='*45}")
        print(f"  ID       : {self.emp_id}")
        print(f"  Name     : {self.name}")
        print(f"  Dept     : {self.dept}")
        print(f"  Salary   : {utils.format_currency(self.salary)}")
        print(f"  Joining  : {self.joining_date}")
        print(f"{'='*45}")

    def give_raise(self,percent):
        old_salary= self.salary
        self.salary = round(self.salary * (1 + percent/100), 2)
        return f" {self.name} salary: {utils.format_currency(old_salary)} → {utils.format_currency(self.salary)}"
    
    def to_csv_row(self):
        return [self.emp_id, self.name, self.dept, self.salary, self.joining_date]
    
class EmployeeManager:
    def __init__(self,filename="employees.csv"):
        self.filename=filename
        self.employees=[]
        self.load_from_file()
    
    def load_from_file(self):
        try:
            with open(self.filename,"r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        emp = Employee(row[0], row[1], row[2], 
                                      float(row[3]), row[4])
                        self.employees.append(emp)
            print(f" {len(self.employees)} employees loaded!")
        except FileNotFoundError:
            print(" New system — no existing data!")
    
    def save_to_file(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            for emp in self.employees:
                writer.writerow(emp.to_csv_row())
        print("Data saved!")
    
    def add_employee(self, emp_id, name, dept, salary):
        joining = datetime.now().strftime("%d-%m-%Y")
        emp = Employee(emp_id, name, dept, salary, joining)
        self.employees.append(emp)
        self.save_to_file()
        return f" {name} added successfully!"
    
    def find_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None
    
    def get_dept_employees(self, dept):
        return [emp for emp in self.employees if emp.dept == dept]
    
    def get_highest_paid(self):
        if not self.employees:
            return None
        return max(self.employees, key=lambda emp: emp.salary)
    
    def print_all(self):
        print(f"\n{'='*55}")
        print(f"{'ID':<8} {'Name':<20} {'Dept':<12} {'Salary'}")
        print(f"{'-'*55}")
        for emp in self.employees:
            print(f"{emp.emp_id:<8} {emp.name:<20} {emp.dept:<12} {utils.format_currency(emp.salary)}")
        print(f"{'='*55}")


manager = EmployeeManager()

print(manager.add_employee("E001", "garvit khuteta", "Data Science", 45000))
print(manager.add_employee("E002", "rahul sharma",   "ML Engineer",  55000))
print(manager.add_employee("E003", "priya singh",    "Data Science", 62000))
print(manager.add_employee("E004", "amit verma",     "HR",           38000))
print(manager.add_employee("E005", "neha joshi",     "ML Engineer",  58000))


manager.print_all()


emp = manager.find_employee("E003")
if emp:
    emp.get_info()


print(manager.employees[0].give_raise(10))


ds_team = manager.get_dept_employees("Data Science")
print(f"\nData Science team:")
for e in ds_team:
    print(f"  → {e.name}")


top = manager.get_highest_paid()
print(f"\n Highest Paid: {top.name} ({utils.format_currency(top.salary)})")


manager.save_to_file()      