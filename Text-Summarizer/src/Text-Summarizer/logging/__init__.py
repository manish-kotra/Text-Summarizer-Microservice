import os
import sys
import logging

logging_str = "[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"
lof_dir = "logs"
log_filepath = os.path.join(lof_dir, "running_logs.log")
os.makedirs(lof_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Text-Summarizer-Logger")


