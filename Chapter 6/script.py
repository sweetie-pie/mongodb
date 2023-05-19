import pymongo
import sys

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = None
dblist = client.list_database_names()

if "users" in dblist:
  print("The users database exists.")

  db = client["users"]
else:
  sys.exit(-1)
