import requests
import logging
from datetime import datetime

logging.basicConfig(filename = "logs/mini_etl.log", level = logging.DEBUG, format = "%(asctime)s | %(levelname)s | %(message)s")

url = "https://jsonplaceholder.typicode.com/users"

logging.info(f"Process Started")

start_time = datetime.now()
total_time = 0
total_count = 0
failed_count = 0
processed_count = 0

try:
    response = requests.get(url,timeout = 5)
    response.raise_for_status()
    logging.info(f"Fetch Successful")
    data = response.json()
except requests.exceptions.HTTPError as e:
    logging.error(f"Couldn't fetch {url}: {e}")
    data = []
for user in data:
    total_count = total_count +1
    try:
        name = user["name"]
        user_id = user["id"]
        email = user["email"]
        phone = user["phone"]
        processed_count = processed_count + 1
        logging.info(f"ID: {user_id} ({name}) Processed Successfully")
    except Exception as e:
        logging.error(f"User Processing Failed due to: {e}")
        failed_count = failed_count + 1
        continue

end_time = datetime.now()
total_time = (end_time - start_time).total_seconds()

print(f"===== Summary =====")
print(f"Total users: {total_count}")
print(f"Processed users: {processed_count}")
print(f"Failed users: {failed_count}")
print(f"Time Taken for processing: {total_time}")
print(f"===================")

logging.info(f"Process Ended")





