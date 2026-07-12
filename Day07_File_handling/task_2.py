file_path = r"\\wsl.localhost\Ubuntu\home\md27\md27\python\sample_data\employees.txt"

with open(file_path,"r") as file:
    for line in file:
        print(line.strip())
