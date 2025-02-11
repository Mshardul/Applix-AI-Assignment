""" File Hander Utility Functions """

# Standard Libraries Imports
import time
import random
from pathlib import Path

UPLOAD_DIR = Path("storage")        # Temporary storage for uploaded files
UPLOAD_DIR.mkdir(exist_ok=True)     # Create if not exists

def random_file_name(file_extension: str) -> Path:
    """ Generate random file names """
    unique_filename = f"{int(time.time())}_{random.randint(10**9, 10**10 - 1)}.{file_extension}"
    file_path: Path = UPLOAD_DIR / unique_filename
    return file_path
