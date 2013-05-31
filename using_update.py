import pymongo
import sys
import datetime

connection = pymongo.MongoClient("mongodb://localhost")

def remove_review_date():
	db = connection.school
        scores = db.scores
        print "removing records with review date"

	try:
		scores.update({},{'$unset':{'review_date':1}}, multi=True)
	except:
		print "Unexpected error:", sys.exc_info()[0]

def using_save():
	db = connection.school
	scores = db.scores
	print "updating records using save"

	try:
		score = scores.find_one({'student_id':1,'type':'homework'})
		print "before ", score
		
		score['review_date'] = datetime.datetime.utcnow()
		scores.save(score)
		
		score = scores.find_one({'student_id':1,'type':'homework'})
		print "after ", score
	except:
		print "Unexpected error:", sys.exc_info()[0]	

def using_update():
	db = connection.school
        scores = db.scores
        print "updating records using update"
	
	try:
		score = scores.find_one({'student_id':1,'type':'homework'})
                print "before ", score

		score['review_date'] = datetime.datetime.utcnow()
		scores.update({'student_id':1,'type':'homework'},score)
		
		score = scores.find_one({'student_id':1,'type':'homework'})
		print "after ", score
	except:
		print "Unexpected error:", sys.exc_info()[0]

def using_set():
	db = connection.school
        scores = db.scores
        print "updating records using set"

        try:
		score = scores.find_one({'student_id':1,'type':'homework'})
                print "before ", score

		scores.update({'student_id':1,'type':'homework'}, {'$set':{'review_date':datetime.datetime.utcnow()}})
		
		score = scores.find_one({'student_id':1,'type':'homework'})
                print "after ", score
        except:
                print "Unexpected error:", sys.exc_info()[0]

remove_review_date()
using_save()
remove_review_date()
using_update()
remove_review_date()
using_set()	
