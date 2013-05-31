import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost")
db = connection.school
foo = db.foo

for i in range (40000, 50000):
	doc = foo.find_one({'student_id':i})
	print "first score for student ", doc['student_id'], " is ", doc['scores'][0]['score'] 