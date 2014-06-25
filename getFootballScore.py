#!/usr/bin/python
import sys
import urllib2
#import libxml2
import lxml.html
import webapp2

def getScoreString():
    url = 'http://www.livefootball.com/'
    html = lxml.html.parse(url)

    matches = html.xpath('//div[contains(@class,"mEl")]//dl')
    ret = []
    for match in matches:
        indiData = match.xpath('.//dd')
        parsedData = []
        for field in indiData:
            parsedData.append(''.join(map(str, field.xpath('.//text()'))))
        for i,x in enumerate(parsedData):
            if x == 'v':
                parsedData[i] = '  v  '
                
        out = '\t'.join(parsedData).strip()
        if len(out) > 0:
            ret.append(out)
    return '\n'.join(ret)

class getFootballScore(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(getScoreString())


application = webapp2.WSGIApplication([
        ('/', getFootballScore),
        ], debug=False)

print getScoreString()
