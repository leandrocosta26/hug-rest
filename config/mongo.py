from pymongo import MongoClient

client = MongoClient('localhost', 27017)

database = client['hug_rest']