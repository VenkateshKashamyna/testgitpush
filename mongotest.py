from pymongo import MongoClient




client = MongoClient("mongodb+srv://admin:admin@clusternameissame.txljzvs.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {"name": "venkat", "age": 25}
d = {"name": "venkat", "age": 25}
d = {"name": "venkat", "age": 25}
collection = db['test-collection']
collection.insert_one(d)

