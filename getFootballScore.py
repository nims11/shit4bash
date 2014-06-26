#!/usr/bin/python
import sys
import webapp2
from google.appengine.api import memcache
from footballMatchesUpdate import getFootballScoreString

class getFootballScore(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(memcache.get('footballScores'))

class updateFootballScore(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        memcache.add('footballScores', getFootballScoreString())
        self.response.write('Updated!')

application = webapp2.WSGIApplication([
        ('/football', getFootballScore),
		('/football/update', updateFootballScore)
        ], debug=False)

