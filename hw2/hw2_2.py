import pymongo
import sys

def remove_lowest_score():
	connection = pymongo.MongoClient("mongodb://localhost")
	db = connection.students
	grades = db.grades

	query = {'type':'homework'}
	cursor = grades.find(query).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])
	
	student_id = -1 
	for doc in cursor:
		if (student_id != doc['student_id']):
			grades.remove(doc['_id'])
		student_id = doc['student_id']	

remove_lowest_score()
