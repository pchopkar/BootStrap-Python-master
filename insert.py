import pymongo
import connect as c
if __name__=="__main__":
    print("Inside insert.py")
    client = c.connectdb()
    #Db Should be created with its name
    db = client["FirsMongoDb"]
    #Collection is called as table on created DB above
    collection = db["ContactUs"]
    #Id created by default with default random key
    #But if you are giving _Id then it will create customize Id on db
    dictionary = {"_id":1,"Name" : "Parjanya", "LastName" : "Chopkar"}
    #You have to create one dictionary format object and insert one row then only you can see table on mongoDb compass
    collection.insert_one(dictionary)