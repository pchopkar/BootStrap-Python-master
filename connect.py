import pymongo

def connectdb() :
#if __name__=="__main__":
    print("Insert connect.py")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print("Connect Done at :" + str(client))
    return client

def connectatlasdb():
    print("Inside Atlas connect function")
    
    client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.sbkseac.mongodb.net/?retryWrites=true&w=majority")
    #db = client.test

    #client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.sbkseac.mongodb.net/?retryWrites=true&w=majority")
    print("Connect Done at :" + str(client))
    print(client.list_database_names())
    return client

 
client = connectatlasdb()
db = client.get_database("FirstMongoDb")
collection = db.ContactUs
dictionary = {"Full Name" : "Parjanya Chopkar", "Email" : "chopkarparjanya@gmail.com", "Message" : "Hello World"}
#You have to create one dictionary for mat object and insert one row then only you can see table on mongoDb compass
collection.insert_one(dictionary)
print("Inserted Successfully")
