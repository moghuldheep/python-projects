import logging
from datetime import datetime
import employee
import os
from file_utils import read_file

logging.basicConfig(filename='logs/employee.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s' )

logging.info("Program started")

def process_summary(total_records, processed_records, failed_records):
        print(f"===============================")
        print(f"Employee ETL System Summary")
        print(f"===============================")
        print(f"Total records: {total_records}")
        print(f"Processed records: {processed_records}")
        print(f"Failed records: {failed_records}")
        print(f"Total processing time: {total_processing_time:.2f} seconds")
        print(f"===============================")
        
process_start_time = datetime.now()
total_processing_time = 0
employees = []
total_records = 0
processed_records = 0
failed_records = 0
lines = read_file()

print(f"Employee ETL System initialized successfully")

for line in lines:
    total_records += 1
    employee_id, name, job, salary = (line.strip().split(","))

    try:
        emp = employee.Employee(employee_id, name, job, salary)
    except ValueError as e:
        logging.error(f"employee_id: {employee_id} | name: {name} | job: {job} | salary: {salary} | Error: {e}")
        failed_records += 1
        continue
    processed_records += 1
    employees.append(emp)

    logging.info(f"Employee created: {name}")

for emp in employees:
    emp.display()
    
process_summary(total_records, processed_records, failed_records)

process_end_time = datetime.now()
total_processing_time = (process_end_time - process_start_time).total_seconds()
logging.info("Program completed")


