import requests
import logging

logging.basicConfig(filename = "logs/processed.log", level = logging.INFO)

logging.info(f"Program started")

print(f"Requests version: {requests.__version__}")

logging.info(f"Program finished")
