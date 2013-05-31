import pymongo

read_pref = pymongo.read_preferences.ReadPreference.SECONDARY

c = pymongo.MongoClient(host="mongodb://localhost:27017", replicaSet="rs1", w=3, j=True, wtimeout=10000, read_preference=read_pref)
db = c.m101
people = db.people

print "inserting"
people.insert({"name":"Cristina", "favorite_color":"silver"})
print "inserting"
people.insert({"name":"Marcela", "favorite_color":"blue"})