import json
import csv

# utils file. i write all the stuff here for saving and loading data.

# loads exercises from a json file
def load_from_json(file_path):
    try:
        # tries to open the file and read the json data
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # if the file doesn’t exist, returns an empty list
        return []

# saves exercises to a json file
def save_to_json(data, file_path):
    # writes the data into the file as json
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# saves exercises to a csv file
def save_to_csv(data, file_path):
    # writes the data into the file as a csv
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "muscle_group", "equipment"])
        writer.writeheader()  # writes the header row
        writer.writerows(data)  # writes all the rows of data