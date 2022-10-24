"""Count the lines of code in our project source directory."""
import os

GPFS_DIRECTORY = "/project/src"

def count_loc_in_file(path):
    """Count the lines of code in the file with the path."""
    result = 0
    with open(path, "r") as stream:
        contents = stream.read()
        result = len(contents.split("\n"))
    return result

def count_loc_in_dir(dir_path):
    "Count the lines of code in all .py files in directory hierarchy"
    result = 0
    for dir in os.listdir(dir_path):
        path = os.path.join(dir_path, dir)
        if os.path.isdir(path):
            result = result + count_loc_in_dir(path)
        elif path.endswith(".py"):
            result = result + count_loc_in_file(path)
    return result

def count_loc():
    """Count the lines of code in .py files in our project."""
    loc = count_loc_in_dir(GPFS_DIRECTORY)
    return loc
