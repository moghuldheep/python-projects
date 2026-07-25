import logging
from datetime import datetime
from employee import Employee
from file_utils import read_file

logging.basicConfig(filename='logs/employee.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s' )
logging.info("Program started")

def process_summary(total_records, processed_records, failed_records, total_processing_time, total_bonus, high_salary_employees):
    return (
        "===============================\n"
        "Employee ETL System Summary\n"
        "===============================\n"
        f"Total records: {total_records}\n"
        f"Processed records: {processed_records}\n"
        f"Failed records: {failed_records}\n"
        f"Total bonus: {total_bonus}\n"
        f"High salary employees: {high_salary_employees}\n"
        f"Total processing time: {total_processing_time:.2f} seconds\n"
        "==============================="
    )
        
process_start_time = datetime.now()
total_processing_time = 0
employees = []
total_records = 0
processed_records = 0
failed_records = 0
lines = read_file()

total_bonus = 0
high_salary_employees = 0

print(f"Employee ETL System initialized successfully")

for record_number, line in enumerate(lines, start=2):
    total_records += 1
    employee_id, name, job, salary = (line.strip().split(","))

    try:
        emp = Employee(employee_id, name, job, salary)
        logging.info(f"record: {record_number} | employee_id: {employee_id} | name: {name} | job: {job} | salary: {salary}")
    except ValueError as e:
        logging.error(f"record: {record_number} | employee_id: {employee_id} | name: {name} | job: {job} | salary: {salary} | Error: {e}")
        failed_records += 1
        continue
    processed_records += 1
    employees.append(emp)

for emp in employees:
    emp.display()
    bonus = emp.calculate_bonus()
    logging.info(f"Bonus: {bonus}")
    print(f"Bonus: {bonus}")
    total_bonus += bonus
    salary_after_raise = emp.give_raise()
    print(f"Salary after raise: {salary_after_raise}")
    logging.info(f"Salary after raise: {salary_after_raise}")
    if emp.is_high_salary():
        print(f"Is high salary: Yes")
        high_salary_employees += 1
    print(f"----------------")

process_end_time = datetime.now()
total_processing_time = (process_end_time - process_start_time).total_seconds()

summary = process_summary(total_records, processed_records, failed_records, total_processing_time, total_bonus, high_salary_employees)
with open('reports/report.txt', 'a', encoding='utf-8') as report_file:
    report_file.write(summary + '\n')

logging.info("Program completed")


