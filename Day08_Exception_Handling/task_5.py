try:
    age = int(input("Enter your age: "))
    print(f"Age: {age}")
except:
    print("Enter a valid number.")
finally:
    print("Program execution completed.")
