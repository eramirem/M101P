import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
people = db.people

def insert():
	print "insert, reporting from duty"
	
	cristina = {'name':'Cristina','company':'TWNN','interest':['computers','politics','economics','journalism']}
	billy = {'_id':'tobon', 'name':'Billy','company':'Viggle','interests':['warhammer','computers','crossfit','ios']}
	
	try:
		people.insert(cristina)
		people.insert(billy)
	except:
		print "Unexpected error ...",sys.exc_info()[0]
	
	print(cristina)
	print(billy)

insert()
