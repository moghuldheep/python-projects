email = input("Enter your email: ")

print(email.startswith("m"))
if email.find("@") == -1:
    print("Invalid email")
else:
    print("Valid email")
