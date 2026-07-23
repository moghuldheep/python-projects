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
        print(f"----------------")

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
        self.salary_after_raise = self.salary + amount
        print(f"{self.salary_after_raise}")
