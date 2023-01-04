"""Generate test data for unit test"""

import os

def generate_test_data():
    """Generate demographics.csv test data file into temp directory for unit test."""

    directory = os.path.join(os.path.dirname(__file__), "gpfs_test")
    delete_temp_directory(directory)
    subdir = f"{directory}/private_info"
    os.makedirs(subdir, exist_ok=True)
    with open(f"{subdir}/demographics.csv", "w+") as fp:
        fp.write("first_name,last_name,address,zip,ssn\n")
        fp.write("john,smith,1 main street,10036,123-45-6789\n")
        fp.write("jane,doe,1 ceder lan,10019,987-65-4321\n")
        fp.write("bob,jones,12 ceder lan,10019,987-65-1234\n")
    return directory

def delete_temp_directory(directory):
    """Delete test data and temp directory to clean up after unit test"""

    remove_file(f"{directory}/private_info/demographics.csv")
    remove_directory(f"{directory}/private_info")
    remove_directory(f"{directory}")

def remove_file(file_path):
    """Remove a file if exists"""
    if os.path.exists(file_path):
        os.remove(file_path)

def remove_directory(dir_path):
    """Remove a directory if exists"""
    if os.path.exists(dir_path):
        os.rmdir(dir_path)
