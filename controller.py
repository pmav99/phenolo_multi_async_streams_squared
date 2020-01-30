import logging
import pathlib
import random
import shlex
import shutil
import subprocess
import time

from concurrent.futures import ProcessPoolExecutor, as_completed

from process_pixel import process_file

logging.basicConfig(level=10)
logger = logging.getLogger(__file__)

root_dir = pathlib.Path(__file__).parent
input_dir = root_dir / "input_dir"
intermediate_dir = root_dir / "intermediate_dir"
gather_output_script = root_dir / "gather_output.py"


### Here we start...!

# First create the process that will be monitoring the intermediate directory for
# new files.
move_to_final_proc = subprocess.Popen(shlex.split(f"python {gather_output_script.as_posix()}"))

# Now create a pool of N processes and start processing the input files
pool_size = 3
with ProcessPoolExecutor(pool_size) as executor:
    futures_to_filepaths = {}
    for filepath in input_dir.glob("*.txt"):
        future = executor.submit(process_file, filepath)
        futures_to_filepaths[future] = filepath

    # wait for the futures to finish
    for future in as_completed(futures_to_filepaths):
        filepath = futures_to_filepaths[future]
        future.result()
        logger.warning(f"{filepath} should be getting moved to final")

# Before exiting, we need to wait for the last intermediate result to be processed/moved.
# There are more elegant ways to ensure this, but I am too bored to implement them :P
time.sleep(2)
move_to_final_proc.kill()

# Done!
