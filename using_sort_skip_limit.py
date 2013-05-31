import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
scores = db.scores

def find():
	print "find, reporting from duty"
	query = {}
	
	try:
		cursor = scores.find(query).skip(4)
		cursor = cursor.limit(1)
		cursor = cursor.sort('student_id',pymongo.ASCENDING).skip(4).limit(1)
	except:
		print "Unexpected error ...",sys.exc_info()[0]
	
	for doc in cursor:
		print doc

find()
