import logging

logging.basicConfig(filename='logs/employee.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def read_file():
    try:
        with open("/home/md27/md27/python/python-projects/Phase01_Capstone/data/employees.csv", "r") as file:
            next(file)  # Skip the header line
            data = file.readlines()
            return data
    except FileNotFoundError:
        logging.error("File not found") 
    except FileNotFoundError:
        logging.error("File not found")