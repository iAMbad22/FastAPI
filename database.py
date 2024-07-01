# database.py
from typing import Optional
import os
from pymongo import MongoClient
from pydantic import BaseModel
from dotenv import load_dotenv
from passlib.context import CryptContext

# Load environment variables from .env file
load_dotenv()

# Define your MongoDB connection (modify the URI accordingly)
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://<username>:<password>@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority")
client = MongoClient(DATABASE_URL)
db = client["fastapi_db"]

# Define a password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Transcript(BaseModel):
    text: str
    user: str
    timestamp: Optional[str]

def get_mongo_db():
    return db

def create_user_in_db(username: str, password: str):
    hashed_password = pwd_context.hash(password)
    db.users.insert_one({"username": username, "hashed_password": hashed_password})

def get_user_from_db(username: str):
    return db.users.find_one({"username": username})
