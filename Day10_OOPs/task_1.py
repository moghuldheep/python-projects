class Employee:

    def __init__(self,name, salary):
        self.name = name
        self.salary = int(salary)
    
employee1 = Employee("Moghul", 50000)
employee2 = Employee("Annie", 52000)

print(employee1.name, employee1.salary)
print(employee2.name, employee2.salary)




