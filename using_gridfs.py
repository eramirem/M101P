import gridfs
import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost")
db = connection.test

def main():
	grid = gridfs.GridFS(db, 'installers')
	fin = open('Skype_6.3.0.602.dmg', 'r')

	_id = grid.put(fin)
	fin.close

	print "id of the file is ", _id

main()