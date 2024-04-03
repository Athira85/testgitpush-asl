import pymongo
client = pymongo.MongoClient("mongodb+srv://athiraslal08:asl&&mongodb@cluster85.zlqt4bk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster85")
db = client.test
print(db)

d = {
    "name":"athira",
    "email":"athira@gmail.com",
    "surname":"manilal"
}
db1 = client['MONGOTEST']
coll = db1['test']
coll.insert_one(d)