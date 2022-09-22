from dotenv import load_dotenv
from os import environ
from pymongo import MongoClient
from flask import Flask, request
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Create the database connection
DB_USER = environ.get("DB_USER")
DB_PASSWORD = environ.get("DB_PASSWORD")
PROJECT_NAME = environ.get("PROJECT_NAME")
DB_HOST = environ.get("DB_HOST")
DB_NAME = environ.get("DB_NAME")

client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{PROJECT_NAME}.{DB_HOST}/?retryWrites=true&w=majority")
db = client[DB_NAME]

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():

    # Get a cursor of records
    records = db["messages"].find()

    # Get all data except the id from each record
    # Bit of a hack, to be honest, with the dictionary comprehension inside the list comprehension
    # Happy to talk through this line if it's confusing
    records = [{ k:v for k,v in r.items() if k != "_id" } for r in records]

    # Return the data
    return records

@app.route("/new", methods=["POST"])
def create():

    # Get the POST body
    new_record = request.get_json()

    # Add the document
    result = db["messages"].insert_one(new_record)

    # Return a stringified ID 
    return str(result.inserted_id), 201

if __name__ == "__main__":
    app.run(debug=True)