import pymongo  

client = pymongo.MongoClient("mongodb://samir:samir2003@ac-ukkwlpc-shard-00-00.lwrx45l.mongodb.net:27017,ac-ukkwlpc-shard-00-01.lwrx45l.mongodb.net:27017,ac-ukkwlpc-shard-00-02.lwrx45l.mongodb.net:27017/?ssl=true&replicaSet=atlas-1cnmsa-shard-0&authSource=admin&retryWrites=true&w=majority")  

#  _____________________________________________________________
# create  database and data
collection = client.samircollection.webpages
booksData = [  
  
      {  
         "id":"01",  
         "language": "Java",  
         "edition": "third",  
         "author": "Herbert Schildt"  
      },  
  
      {  
         "id":"07",  
         "language": "C++",  
         "edition": "second",  
         "author": "E.Balagurusamy"  
      }  
   ]  
  
collection.insert_many(booksData) 

# ____________________________________________________________

# create data
data={"id":"55","language":"marathi"}

create = client.samircollection.webpages
create.insert_one(data)
# ____________________________________________________________

# read data
read = client.samircollection.webpages.find_one({"id":"77"})
print(read)
# ___________________________________________________________

# update data
update = client.samircollection.webpages.update_one({"id":"55"},{"$set":{"id":"60"}})
# __________________________________________________________

# delete data
delete = client.samircollection.webpages.delete_one({"id":"60"})
print(delete)


