import csv
import logging
import requests

logging.basicConfig(filename = "processed.log",
                    level = logging.DEBUG,
                    format = "%(asctime)s | %(levelname)s | %(message)s"
                    )
logging.info(f"Program started!")

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url,timeout = 5)
    response.raise_for_status()
    logging.info(f"Fetch Successful")
    data = response.json()
except requests.exception.HTTPError as e:
    logging.error(f"Fetch Failed - {url}: {e}")
    data =[]

count = 0

try:
    with open ("users.csv", "w", newline = "", encoding = "utf-8") as file:
        logging.info(f"Writing CSV")
        writer = csv.writer(file)
        writer.writerow(["id", "name", "email"])
        for user in data:
            count = count + 1
            writer.writerow([
                user["id"],
                user["name"],
                user["email"]
                ])
        logging.info(f"CSV File write complete")
except Exception as e :
    logging.error(f"Couldnt write to CSV: {e}")
        
print(f"Number of users: {count}")
logging.info(f"Number of users written: {count}")

with open("users.csv","r", encoding = "utf-8") as file:
    for line in file:
        print(line)

logging.info(f"Program Completed")

