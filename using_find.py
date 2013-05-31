import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
scores = db.scores

def find():
	print "find, reporting from duty"
	query = {'type':'exam'}
	selector = {'student_id':1, 'score':1, '_id':0}
	
	try:
		cursor = scores.find(query,selector)
	except:
		print "Unexpected error",sys.exc_info()[0]

	sanity = 0
	for doc in cursor:
		print doc
		sanity += 1
		if (sanity > 10):
			break	

def find_one():
	print "find one, reporting from duty"
	query = {'student_id':10}
	
	try:
		doc = scores.find_one(query)
	except:
		print "Unexpected error",sys.exc_info()[0]
	print doc

find()
