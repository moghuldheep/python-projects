import requests
import logging

logging.basicConfig(filename="logs/task.log", level=logging.DEBUG, format = "%(asctime)s | %(levelname)s | %(message)s")

url = "https://jsonplaceholder.typicode.com/users"
new_user = {
        "name": "Moghul",
        "email": "moghuldheepb@gmail.com",
        "phone": "9988811224"
        }
try:
    logging.info(f"Sending request")
    response = requests.post(url, json=new_user)
    if response.status_code == 201:
        print(f"Request Successfull")
        logging.info(f"Request Successfull!")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    logging.info(f"Request failed!")
    exit()

print(response.status_code)
print(response.json())
