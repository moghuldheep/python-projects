import requests
import logging
from datetime import datetime

logging.basicConfig(filename="logs/mini_etl.log", level=logging.DEBUG, format="%(asctime)s | %(levelname)s | %(message)s")

url = "https://jsonplaceholder.typicode.com/users"

try:
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    phone = input("Enter user phone: ")
    logging.info(f"Received user input successfully")

except ValueError:
    print(f"Enter valid input")
    logging.info(f"User input not valid")
    exit()

start_time = datetime.now()
total_time = 0

new_user = {
        "name" : name,
        "email" : email,
        "phone" : phone
        }
logging.info(f"Dictionary created with user input")

try:
    response = requests.post(url, json=new_user)
    logging.info(f"Sending Request")
    if response.status_code == 201:
        data = response.json()
        print(f"Id assigned: {data['id']}")
        print(f"Employee created: {data}")
        logging.info(f"Request Successfull!")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    logging.info(f"Request failed!")
    exit()

end_time = datetime.now()
total_time = (end_time - start_time).total_seconds()

print(f"====== Summary ======")
print(f"Status Code: {response.status_code}")
print(f"Id assigned: {data["id"]}")
print(f"Employee created: {data}")
print(f"Processing time: {total_time}")





