import json
import urllib2
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.reddit
stories = db.stories

reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")
parsed = json.loads(reddit_page.read())

for item in parsed['data']['children']:
	stories.insert(item['data'])
