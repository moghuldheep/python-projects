import requests
import logging

logging.basicConfig(filename = "logs/processed.log", level = logging.DEBUG, format = "%(asctime)s | %(levelname)s | %(message)s")

url = "https://jsonplaceholder.typicode.com/users"

try:
    user_id = int(input("Enter the user_id to search: "))
except ValueError:
    print(f"Enter a valid userid")
    exit()

params = {
        "id": user_id
        }
try:
    response = requests.get(url,params = params,timeout = 5)
    response.raise_for_status()
    logging.info(f"Fetching userid: {user_id}")
    
    data = response.json()

    if not data:
        print(f"The user_id you searched for do not exist")
        logging.info(f"Fetch Failed! {user_id} do not exist")
    else:
        name = data[0]["name"]
        user_id = data[0]["id"]
        email = data[0]["email"]
        phone = data[0]["phone"]
        logging.info(f"Fetch successfull for userid: {user_id}!")

        print(f"User Id: {user_id}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")

except requests.exceptions.RequestException as e:

    logging.error(f"Couldn't fetch {user_id}: {e}")
