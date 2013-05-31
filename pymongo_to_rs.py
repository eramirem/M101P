import pymongo
import sys

c = pymongo.MongoClient(host="mongodb://localhost:27019", replicaSet="rs1", w=1, j=True)
db = c.m101
people = db.people

try:
	print "inserting"
	people.insert({"name":"Billy Tobon", "favorite_color":"orange"})
	print "inserting"
	people.insert({"name":"Otila Martinez", "favorite_color":"green"})
except:
	print "Unexpected error: ", sys.exc_info()[0]
print "completed the inserts"