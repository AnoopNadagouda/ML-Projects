import logging
import os
from datetime import datetime
from src.logger import logging

# Define the log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a path for the logs folder
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the directory even if it already exists
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

LOG_FILE = os.path.join(logs_path, LOG_FILE)

# Configure the logging behavior
logging.basicConfig(
    filename=LOG_FILE,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


import sys
from src.logger import logging
from src.exceptions import CustomException

