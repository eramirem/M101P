import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost")
db = connection.school
students = db.students

cursor = students.find()

student_id = -1
for doc in cursor:
	if doc['_id'] != student_id: 
		student_id = doc['_id']
		min_score = 100	
		for scores in doc['scores']:
			if scores['type'] == 'homework':
				if  min_score > scores['score']:
					min_score = scores['score']
					min_doc = scores
		doc['scores'].remove(min_doc)
		students.save(doc)

				
