try:
    num3 = int(input("Enter your number: "))

    print(100 / num3)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Please enter a non zero number.")
