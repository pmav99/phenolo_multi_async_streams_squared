import logging
import random
import shutil
import time

logging.basicConfig(level=10)
logger = logging.getLogger(__file__)


def process_file(filepath):
    logger.info(f"Starting to process {filepath}")
    time.sleep(random.randint(1, 2))
    shutil.move(filepath.as_posix(), intermediate_dir.as_posix())
    logger.info(f"Finished processing {filepath}")
