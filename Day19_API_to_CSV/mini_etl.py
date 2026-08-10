import csv
import logging
import requests
from datetime import datetime

logging.basicConfig(filename = "logs/processed.log",
                    level = logging.DEBUG,
                    format = "%(asctime)s | %(levelname)s | %(message)s"
                    )
logging.info(f"Program started!")
start_time = datetime.now()
total_time = 0
failed_count = 0
processed_count = 0
count = 0

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url,timeout = 5)
    response.raise_for_status()
    logging.info(f"Fetch Successful")
    data = response.json()
except requests.exception.HTTPError as e:
    logging.error(f"Fetch Failed - {url}: {e}")
    data =[]

try:
    with open ("logs/users.csv", "w", newline = "", encoding = "utf-8") as file:
        logging.info(f"Writing CSV")
        writer = csv.writer(file)
        writer.writerow(["id", "name", "email", "company"])
        for user in data:
            count = count + 1
            logging.info(f"Writing employee {id}")
            try:
                writer.writerow([
                    user["id"],
                    user["name"],
                    user["email"],
                    user["company"]
                    ])
                logging.info(f"Writing employee {id} Successful")
                processed_count = processed_count + 1
            except Exception as e:
                failed_count = failed_count + 1
                logging.info(f"Employee {id} Failed - {e}")
        logging.info(f"CSV File write complete")
except Exception as e :
    logging.error(f"Couldnt write to CSV: {e}")

print(f"Number of users: {count}")
logging.info(f"Number of users written: {count}")

with open("users.csv","r", encoding = "utf-8") as file:
    for line in file:
        print(line)

logging.info(f"Program Completed")
end_time = datetime.now()
total_time = (end_time - start_time).total_seconds()

print(f"-----Summary-----")
print(f"Total users: {count}")
print(f"Written: {processed_count}")
print(f"Failed: {failed_count}")
print(f"Time taken: {total_time}")
