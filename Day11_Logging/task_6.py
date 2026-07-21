import logging

logging.basicConfig(filename = "employee_processed.log",
                    level = logging.DEBUG,
                    format = "%(asctime)s | %(levelname)s | %(message)s"
                    )

file_path = "/home/md27/md27/python/python-projects/Day10_OOPs/employees.csv"

with open(file_path,"r") as file:

    next(file)

    for line in file:

        columns = line.strip().split(",")

        try:
            employee_id = columns[0]
            name = columns[1]
            job = columns[2]
            salary = int(columns[3])

            logging.info(f"Processing {name}.")
            logging.debug(f"Salary: {salary}.")
        except ValueError:
            logging.error(f"Invalid salary for {name}")
