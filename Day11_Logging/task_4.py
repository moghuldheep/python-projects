import logging

logging.basicConfig(level = logging.INFO)

file_path = "/home/md27/md27/python/python-projects/Day10_OOPs/employees.csv"

with open(file_path,"r") as file:

    next(file)

    for line in file:

        employee_id, name, job, salary = line.strip().split(",")

        logging.info(f"Processing {name}.")
        
