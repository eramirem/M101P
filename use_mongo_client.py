import pymongo

c = pymongo.MongoClient(host="mongodb://localhost:27017", w=1, j=True)
db = c.m101
people = db.people

print "inserting"
people.insert({"name":"Elizabeth Ramirez", "favorite_color":"white"})
print "inserting"
people.insert({"name":"Valentina Ramirez", "favorite_color":"pink"})
print "inserting"
people.insert({"name":"Claudia Ramirez", "favorite_color":"blue"})