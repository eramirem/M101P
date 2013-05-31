import bottle
@bottle.route('/')
def home_page():
	mythings = ['apple','orange','banana','pear']
	return bottle.template('hello_world', {'username':'Elizabeth', 'things':mythings})
bottle.debug(True)
bottle.run(host='localhost',port=8080)
