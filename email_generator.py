import sys

# Check if a filename argument is provided
if len(sys.argv) > 1:
    # If first argument looks like a filename (contains .txt), use it as the file
    if sys.argv[1].endswith('.txt'):
        filename = sys.argv[1]
        names_list = []
        with open(filename, "r") as file:
            names_list = file.readlines()
        
        print(f"\nGenerated emails from {filename}:")
        for full_name_line in names_list:
            names = full_name_line.strip().split()
            if names:
                email = ".".join([name.lower() for name in names]) + "@mdb.com"
                print(f"{' '.join(names)} -> {email}")
    else:
        # Process as individual names
        full_name = sys.argv[1:]
        print("Hello! ", " ".join(full_name))
        email = ".".join([name.lower() for name in full_name]) + "@mdb.com"
        print("Your email address is: ", email)
else:
    # If no arguments, read from default file
    with open("employee_list.txt", "r") as file:
        names_list = file.readlines()
    
    print("\nGenerated emails for new joinees:")
    for full_name_line in names_list:
        names = full_name_line.strip().split()
        if names:
            email = ".".join([name.lower() for name in names]) + "@mdb.com"
            print(f"{' '.join(names)} -> {email}")