class Employee:

    def __init__(self, employee_id, name, job, salary):
        self.employee_id = employee_id
        self.name = name
        self.job = job
        self.salary = int(salary)

    def display(self):
        print(f"Employee details")
        print(f"----------------")
        print(self.name)
        print(self.job)
        print(self.salary)

    def calculate_bonus(self):
        if self.salary >= 50000:
            return int(self.salary * 0.10)
        else:
            return int(self.salary * 0.05)

    def is_high_salary(self):
        return self.salary >=50000

    def give_raise(self, amount):
        old_salary = self.salary
        print(f"{old_salary}")
        self.salary = self.salary + amount
        print(f"{self.salary}")


file_path = "/home/md27/md27/python/python-projects/Day10_OOPs/employees.csv"

employees = []

with open(file_path, "r") as file:

    next(file)

    for line in file:

        employee_id, name, job, salary = line.strip().split(",")
    
        employee = Employee(employee_id, name, job, salary)

        employee.display()

        print(employee.calculate_bonus())

        print(employee.is_high_salary())
        
        employee.give_raise(5000)
