import csv

"""Folder in our large project GPFS file system"""
GPFS_FOLDER = "/myproject_data"

def find_people(search_zip_code):
    """Find people that live in a specific zip code and return their demographic information"""

    result = []
    demographics_csv = f"{GPFS_FOLDER}/private_info/demographics.csv"
    with open(demographics_csv) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            zip_code = row[3]
            if zip_code == search_zip_code:
                result.append(row)
    return result


