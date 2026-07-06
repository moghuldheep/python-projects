try:
    age = int(input("Enter your age: "))
    print(f"Age: {age}")
    
except ValueError:
    print("Please enter a valid age.")
