from pymongo import MongoClient

cluster = "mongodb://192.168.2.2:27017/"

client = MongoClient(cluster)

db = client["test"]

print(db)

todos = db["kevsrobots"]

print(todos)

items = [{"name": "robot1", "type": "robot", "price": 1000},
         {"name": "robot2", "type": "robot", "price": 2000},]

# todos.insert_many(items)

# result = todos.delete_many({"name": "robot1"})

result = todos.update_one({"name": "robot2"}, {"$set": {"status": "active"}})
results = todos.find({})

for result in results:
    print(result)