import os
import sys
import logging
from datetime import datetime

LOG_FORMAT = "[%(asctime)s] %(levelname)s - %(module)s - %(message)s"

LOG_DIR = "logs"
LOG_FILENAME = f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_FILEPATH = os.path.join(LOG_DIR, LOG_FILENAME)

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILEPATH),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("house_price_intel")