# ecommerce_project/mongo.py
from mongoengine import connect
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/ecommerce_db")

def mongo_connect():
    from mongoengine.connection import _connections
    if 'default' not in _connections:
        connect(host=MONGO_URL)
        print(f"Connected to MongoDB at: {MONGO_URL}")
    else:
        print("MongoDB default connection already exists. Skipping connect.")