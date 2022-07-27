import pymongo
client = pymongo.MongoClient("mongodb+srv://Bhanu:Mongo29@cluster0.sq6m3.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"bhanu",
    "email":"bhanu@gmail.com",
    "surname":"dhiman"
}

db1=client['mongotest']
coll = db['test']
coll.insert_one(d)
