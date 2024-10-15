import os

class Config:
    MONGO_URI = os.getenv('MONGODB_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
