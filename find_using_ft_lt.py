import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
scores = db.scores

def find():
	print "find, reporting from duty"
	query = {'type':'exam','score':{'$gt':50,'$lt':70}}
	try:
		cursor = scores.find(query)
	except:
		print "Unexpected error ...",sys.exc_info()[0]
	sanity = 0
	for doc in cursor:
		print doc
		sanity += 1
		if (sanity > 10):
			break

find()		
