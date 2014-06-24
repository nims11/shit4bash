#!/usr/bin/python
import sys
import urllib2
import libxml2

url = 'http://www.livefootball.com/'
f = urllib2.urlopen(url)
html = f.read()
f.close()

parse_options = libxml2.HTML_PARSE_RECOVER + \
		libxml2.HTML_PARSE_NOERROR + \
		libxml2.HTML_PARSE_NOWARNING
doc = libxml2.htmlReadDoc(html, '', None, parse_options)
matches = doc.xpathEval('//div[contains(@class,"mEl")]//dl')

for match in matches:
    indiData = match.xpathEval('.//dd')
    parsedData = []
    for field in indiData:
        parsedData.append(''.join(map(str, field.xpathEval('.//text()'))))
    for i,x in enumerate(parsedData):
        if x == 'v':
            parsedData[i] = '  v'
            
    out = '\t'.join(parsedData).strip()
    if len(out) > 0:
        print out

