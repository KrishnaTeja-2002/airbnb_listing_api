# app.py
from flask import Flask, request, jsonify
from utils.data_utils import read_json, read_csv, write_json, write_csv

app = Flask(__name__)

# Load Airbnb data
JSON_FILE = 'data/airbnb.json'
CSV_FILE = 'data/airbnb.csv'
FIELDNAMES = ['id', 'name', 'price', 'neighborhood', 'host_id', 'room_type']

airbnb_data_json = read_json(JSON_FILE)
airbnb_data_csv = read_csv(CSV_FILE)

# RESTful API Endpoints
# (Implementation of endpoints omitted for brevity)

if __name__ == '__main__':
    app.run(debug=True)
