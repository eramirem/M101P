import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.reddit
stories = db.stories

def find():
	print "find, reporting from duty"
	query = {'media.oembed.type': 'video'}
	selector = {'title':1, 'media.oembed.type':1, '_id':0}
	
	try:
		cursor = stories.find(query,selector)
	except:
		print "Unexpected error ...",sys.exc()[0]
	
	for doc in cursor:
		print doc

find()
