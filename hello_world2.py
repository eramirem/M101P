import bottle

@bottle.route('/')
def home_page():
	return "<html><title></title><body>Hello world\n</body></html>"

@bottle.route('/testpage')
def test_page():
	return "This is a test page\n"

bottle.debug(True)
bottle.run(host='localhost', port=8080)
