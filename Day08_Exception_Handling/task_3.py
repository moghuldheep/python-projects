try:
    with open("employees.txt","r") as file:
        print(file.read())
except:
    print("File does not exist.")
