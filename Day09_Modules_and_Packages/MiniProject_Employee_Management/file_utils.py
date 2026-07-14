def read_employee_file():
    try:
        file_path = "/home/md27/md27/python/sample_data/employees.txt"
        with open(file_path,"r") as file:
                return file.read()
    except FileNotFoundError:
        print(f"File not found.")
