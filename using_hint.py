import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test
foo = db.foo

query = {'a': 4000, 'b': 4000, 'c': 4000}
try:
	doc = foo.find(query).hint([('c', pymongo.ASCENDING)]).explain()
except:
	print 'Unexpected error ', sys.exc_info()[0]

for key in doc:
	print str(key).rjust(20), ": ", str(doc[key])