# mongo_connection.py
import os

from pymongo import MongoClient

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME', 'root')
MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD', 'root')

client = MongoClient(MONGO_URI, username=MONGO_DB_USERNAME, password=MONGO_DB_PASSWORD)
db = client['student_service']

if 'students' not in db.list_collection_names():
    db.create_collection('students')

students_collection = db['students']
