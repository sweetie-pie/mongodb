import pymongo
import sys


# connecting to mongodb
client = pymongo.MongoClient("mongodb://mongodb:27017/")


# get list of databases
db = None
dblist = client.list_database_names()

# find users database
if "users" in dblist:
  print("The users database exists.")

  db = client["users"]
else:
  sys.exit(-1)
