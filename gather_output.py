#!/usr/bin/python
#
# Monitor intermediate_output directory and as soon as a file appears copy it to the final_output directory
#

import logging
import shutil

from watchgod import run_process, DefaultWatcher, watch, Change

logging.basicConfig(level=20)
logger = logging.getLogger("gather_output")


for changes_set in watch('./intermediate_dir/'):
    logger.info(f"Changes in the directory: {changes_set}")
    for (change_type, filename) in changes_set:
        if change_type is not Change.added:
            logger.debug(f"No new file was added. Ignoring change: {filename}")
            continue
        shutil.move(filename, "./output_dir")
        logger.warning(f"Moved {filename} to final the final output directory")

