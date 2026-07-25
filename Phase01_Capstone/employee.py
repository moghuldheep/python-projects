class Employee:

    def __init__(self, employee_id, name, job, salary):
        self.employee_id = employee_id
        self.name = name
        self.job = job
        self.salary = int(salary)

    def calculate_bonus(self):
        if self.salary >= 50000:
            return int(self.salary * 0.10)
        else:
            return int(self.salary * 0.05)

    def is_high_salary(self):
        return self.salary >=50000

    def give_raise(self):
        if self.is_high_salary():
            self.salary = self.salary + self.salary * 0.10
        else:
            self.salary = self.salary + self.salary * 0.05
        return int(self.salary)

    def display(self):
            print(f"Employee details")
            print(f"----------------")
            print(f"Employee Id: {self.employee_id}")
            print(f"Name: {self.name}")
            print(f"Job: {self.job}")
            print(f"Salary: {self.salary}")