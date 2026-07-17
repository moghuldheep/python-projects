class Employee:

    def __init__(self,name, salary):
        self.name = name
        self.salary = int(salary)

    def display(self):
        print(f"Employee Details")
        print(f"----------------")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}\n")

    def calculate_bonus(self):
        if self.salary >= 50000:
            return int(self.salary * 0.10)
        else:
            return int(self.salary * 0.5)

    def is_high_salary(self):
        return self.salary >= 70000

employees = []

with open("/home/md27/md27/python/python-projects/Day10_OOPs/employees.csv", "r") as file:
    
    next(file)
    
    for line in file:
        
        employee_id, name, job, salary = line.strip().split(",")

        employee = Employee(name, salary)
        
        employees.append(employee)

        print(employee.name, employee.salary)

