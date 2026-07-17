correct_password = "python123"
user_password = input("Enter password: ")
while user_password != correct_password:
    print("Wrong Password. Try Agian!")
    user_password = input("Enter password: ")
else:
    print("Access Granted! :)")
