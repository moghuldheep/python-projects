import logging

logging.basicConfig(filename = "processed.log",
                    level = logging.DEBUG,
                    format = "%(asctime)s | %(levelname)s | %(message)s"
                    )

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

logging.info(f"--------Program started!--------")

file_path = "/home/md27/md27/python/python-projects/Day10_OOPs/employees.csv"

employees = []

try:

    with open(file_path, "r") as file:

        next(file)

        for line in file:
            try:
                
                employee_id, name, job, salary = line.strip().split(",")
                
                logging.info(f"Successfully read data for {name}.")

                employee = Employee(employee_id, name, job, salary)
            
                employees.append(employee)
                
                logging.info(f"Employee {name} appended to the employee list.")

            except ValueError:

                logging.error(f"Invalid salary for {name}")
    
    for employee in employees:
        try:
                
            logging.info(f"Started processing {employee.name}")

            employee.display()

            print(employee.calculate_bonus())
                
            logging.info(f"Bonus calculated: {employee.calculate_bonus()}")

            print(employee.is_high_salary())

            employee.give_raise(5000)

        except Exception as e:

            logging.error(f"Unexcepted error {e}")

except FileNotFoundError:
    logging.error(f"File not found")
finally:
    logging.info(f"--------Program completed!--------")
