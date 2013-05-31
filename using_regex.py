import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.reddit
stories = db.stories

def find():
	print "find, reporting from duty"
	query = {'title':{'$regex':'Mozilla'}}

	selector = {'title':1, '_id':0}
	
	try:
		cursor = stories.find(query,selector)
	except:
		print "Unexpected error ...",sys.exc_info()[0]
	
	for doc in cursor:
		print doc

find()
