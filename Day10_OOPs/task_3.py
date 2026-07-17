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

employee1 = Employee("Moghul", 50000)
employee2 = Employee("Annie", 52000)

print(employee1.calculate_bonus())
