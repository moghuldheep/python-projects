class Employee:

    def __init__(self,name, salary):
        self.name = name
        self.salary = int(salary)
        
    def display(self):
        print(f"Employee Details")
        print(f"----------------")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}\n")

employee1 = Employee("Moghul", 50000)
employee2 = Employee("Annie", 52000)

employee1.display()
employee2.display()
