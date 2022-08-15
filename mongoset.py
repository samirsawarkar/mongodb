import pymongo  
client = pymongo.MongoClient("mongodb://samir:samir2003@ac-ukkwlpc-shard-00-00.lwrx45l.mongodb.net:27017,ac-ukkwlpc-shard-00-01.lwrx45l.mongodb.net:27017,ac-ukkwlpc-shard-00-02.lwrx45l.mongodb.net:27017/?ssl=true&replicaSet=atlas-1cnmsa-shard-0&authSource=admin&retryWrites=true&w=majority")  


# collection = client.samircollection.webpages
# booksData = [  
  
#       {  
#          "id":"01",  
#          "language": "Java",  
#          "edition": "third",  
#          "author": "Herbert Schildt"  
#       },  
  
#       {  
#          "id":"07",  
#          "language": "C++",  
#          "edition": "second",  
#          "author": "E.Balagurusamy"  
#       }  
#    ]  
  
# collection.insert_many(booksData)  
# data={"id":"55","language":"marathi"}

# create = client.samircollection.webpages
# create.insert_one(data)

read = client.samircollection.webpages.find_one({"id":"77"})
print(read)
# update = client.samircollection.webpages.update_one({"id":"55"},{"$set":{"id":"60"}})

# delete = client.samircollection.webpages.delete_one({"id":"60"})
# print(delete)


read = client.samircollection.webpages.find_one({"id":"55"})
print(read)