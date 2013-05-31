import pymongo
import sys

def main():
	connection = pymongo.MongoClient("mongodb://localhost",safe=True)
	db = connection.m101
	people = db.people

	person = {"name":"Joe Biden", "role":"Vice President", "address":{"address1":"The White House","street":"1600 Pennsylvania Avenue","state":"DC","city":"Washington"}, "interests":["government","baseball","debates"]}
	people.insert(person)

main()
