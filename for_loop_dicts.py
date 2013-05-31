person = {'name':'Elizabeth R','favorite_color':'white','hair':'black','interests':['tv','books','beer']}
for key in person:
	if (key == 'interests'):
		print "Interests ..."
		for interest in person[key]:
			print "\tinterest is " + interest
	else:
		print "key is " + key + " value is " + person[key]

