import logging
import os
from datetime import datetime

# 1. Create just the filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the 'logs' folder path in your current directory
logs_path = os.path.join(os.getcwd(), "logs")

# 3. Create the 'logs' folder if it doesn't exist
# We don't use the filename here, just the folder path!
os.makedirs(logs_path, exist_ok=True)

# 4. Join the folder and the filename to get the full file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 5. Setup the logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
