import logging
import os
from datetime import datetime

# Create logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Define log file path
log_file = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_file_path = os.path.join(logs_dir, log_file)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format='%(asctime)s: %(levelname)s: %(message)s',
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging setup complete. Log file created at: %s", log_file_path)
    print(f"Log file created at: {log_file_path}")
    logging.info("This is an info message.")
    logging.error("This is an error message.")
    logging.warning("This is a warning message.")
    logging.debug("This is a debug message.")
    logging.critical("This is a critical message.")
