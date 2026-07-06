try:
    file_path = r"\\wsl.localhost\Ubuntu\home\md27\md27\python\sample_data\employee_salary.txt"

    with open(file_path,"r") as file:
        for line in file:
            try:
                columns = line.split(",")
                name = columns[1]
                salary = int(columns[2])
                print(f"Employee: {name}")
                print(f"Salary: {salary}\n")
            except ValueError:
                print(f"Invalid Salary for {name}. Skipping the record.\n")
except FileNotFoundError:
    print(f"File not found.")
