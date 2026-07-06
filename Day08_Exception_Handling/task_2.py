try:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    print(f"Result: {num1/num2}")
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Please enter a non zero number.")
