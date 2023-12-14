# utils/data_utils.py
import json
import csv

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_csv(file_path):
    with open(file_path, 'r') as file:
        data = list(csv.DictReader(file))
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def write_csv(file_path, data, fieldnames):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
