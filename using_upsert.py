import pymongo
import sys
import datetime

connection = pymongo.MongoClient("mongodb://localhost")

def using_upsert():
	db = connection.test
	things = db.things
	print "updating records using upsert"

	try:
		things.drop()
		things.update({'thing':'apple'},{'$set':{'color':'red'}},upsert=True)
		things.update({'thing':'pear'},{'$set':{'color':'green'}},upsert=True)

		apple = things.find_one({'thing':'apple'})
		print apple
		pear = things.find_one({'thing':'pear'})
		print pear
	except:
		print "Unexpected error:", sys.exc_info()[0]	

using_upsert()	
