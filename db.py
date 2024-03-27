from pymongo import MongoClient
import json

# import authentication data
with open('./infos.json') as f:
    infos = json.load(f)
    mongodb = infos['mongodb']
    mongoUusername = mongodb['username']
    mongoPpassword = mongodb['password']
    mongoUrl = mongodb['connectionString']

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = mongoUrl
 
   # Create a connection using MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database 
   return client["bachelorarbeit"]
  


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()