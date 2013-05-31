import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

j = {"firstname" : "Elizabeth", "last_name" : "Ramirez"}
try:
	users.insert(j)
except:
	print "insert failed:",sys.exc_info()[0]
print j
try:
	users.insert(j)
except:
	print "insert failed:",sys.exc_info()[0]
