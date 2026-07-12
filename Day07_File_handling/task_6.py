with open(file_path,"r") as file:
    for line in file:
        columns = line.strip().split(",")
        print(f"Welcome {columns[1]}!\n\nYou work as a {columns[2]}\n\n------------------")
