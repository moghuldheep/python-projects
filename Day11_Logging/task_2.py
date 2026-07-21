import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program Started")
logging.debug("Parsed value is 12")
logging.error("Invalid record. Skipping record")
logging.warning("No valid data, proceeding with default value")
logging.critical("Connection lost")
