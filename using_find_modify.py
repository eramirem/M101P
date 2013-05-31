import pymongo

def get_next_sequence_number(name):
	connection = pymongo.MongoClient("mongodb://localhost")
	db = connection.test
	counters = db.counters
	
	counter = counters.find_and_modify({'type':name},{'$inc':{'value':1}},upsert=True,new=True)

	counter_value = counter['value']
	return counter_value

print get_next_sequence_number('pid')
print get_next_sequence_number('pid')
