class Company:
    def __init__(self, company_name, company_id):
        self.company_name = company_name
        self.company_id = company_id
        
    def accept(self):
        print()
        self.company_name = input("Enter Company Name: ")
        self.company_id = input("Enter Company ID: ")

    def display(self):
        print("Company Name:", self.company_name)
        print("Company ID:", self.company_id)
        
class Employee(Company):
    def __init__(self, employee_name, employee_id, hours_worked):
        super().__init__("", "")
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.hours_worked = hours_worked

    def accept(self):
        super().accept()
        self.employee_name = input("Enter Employee Name: ")
        self.employee_id = input("Enter Employee ID: ")
        self.hours_worked = float(input("Enter Hours Worked: "))

    def display(self):
        print()
        super().display()
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)
        print("Hours Worked:", self.hours_worked)
        print()

    def calculate_salary(self, hourly_rate):
        return self.hours_worked * hourly_rate

    def searchbyeid(self,eid):
      if eid == self.employee_id:
        super().display()
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)
        print("Hours Worked:", self.hours_worked)
        
    def searchbyname(self,namee):
      if namee == self.employee_name:
        super().display()
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)
        print("Hours Worked:", self.hours_worked)
        
    def searchbyhrs(self,workhrs):
      if workhrs == self.hours_worked:
        super().display()
        print("Employee Name:", self.employee_name)
        print("Employee ID:", self.employee_id)
        print("Hours Worked:", self.hours_worked)

# Accepting Employee Info
Employees = []
num_employees = int(input("\nEnter the number of employees: "))
for _ in range(num_employees):
    employee = Employee("", "", 0)
    employee.accept()
    Employees.append(employee)

for i in range(num_employees):
  Employees[i].display()

n=int(input("On what basis you want to diplay information of the employees??.Enter 1 for ID. 2 for Name. 3 for Working Hours. => "))
if n==1:
  eid = input("Enter the Employee id to be searched ")
  for i in range(num_employees):
    Employees[i].searchbyeid(eid)
elif n==2:
  namee = input("Enter the name to be searched ")
  for i in range(num_employees):
    Employees[i].searchbyname(namee)
elif n==3:
  workhrs = float(input("Enter the working hours to be searched "))
  for i in range(num_employees):
    Employees[i].searchbyhrs(workhrs)
   



# Calculating and Displaying Salary
hourly_rate = float(input("\nEnter Hourly Rate: "))
for employee in Employees:
    salary = employee.calculate_salary(hourly_rate)
    print(f"{employee.employee_name}'s Salary:", salary)
