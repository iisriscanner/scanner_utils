import os
import ntpath
import platform
from datetime import datetime
from pathlib import Path

def flatten(input_list):
    return [item for sublist in input_list for item in sublist]

def fix_path(path):
    if platform.system().lower() == 'windows':
        return path.replace(os.sep,ntpath.sep)
    else:
        return path
    
def get_files(path, extensions):
    all_files = []
    for ext in extensions:
        all_files.extend(Path(path).glob(f"*.{ext}"))
    return all_files


def get_time_date_now():
    return datetime.now().strftime('%d-%b-%Y_%H-%M-%S')

def get_time_now():
    return datetime.now().strftime('%d%H%M%S')


def remove_special_characters(phrase):
    t = ""
    for i in phrase:
        # Store only valid characters
        if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i == ' '):
            t += i
    return t


def read_instances(dir_path):
    files = get_files(dir_path, "json")


