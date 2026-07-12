file_path = r"\\wsl.localhost\Ubuntu\home\md27\md27\python\sample_data\employees.txt"

with open(file_path,"r") as file:
    for line in file:
        columns = line.strip().split(",")
        print(f"Employee_id: {columns[0]}")
        print(f"Employee_name: {columns[1]}")
        print(f"Employee_job: {columns[2]}")
