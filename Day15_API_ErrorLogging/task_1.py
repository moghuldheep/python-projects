import requests
import logging

logging.basicConfig(filename = "logs/processed.log", level = logging.DEBUG, format = "%(asctime)s | %(levelname)s | %(message)s")

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url,timeout = 5)

    response.raise_for_status()
    
    logging.info(f"Fetch Successful")

    data = response.json()

except requests.exceptions.HTTPError as e:
    
    logging.error(f"Couldn't fetch {url}: {e}")

count = 0

for user in data:
    
    count = count + 1

print(f"Nmber of users: {count}")

print(f"Name of 1st user: {data[0]["name"]}")




