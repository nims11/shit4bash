#!/usr/bin/python
import urllib2
#import libxml2
import lxml.html

def getFootballScoreString():
    url = 'http://www.livefootball.com/'
    content = urllib2.urlopen(url).read()
    html = lxml.html.fromstring(content)

    matches = html.xpath('//div[contains(@class, "sdHpItem")]/div[contains(@class,"mEl")]//dl[dd]')
    parsedList = []
    for match in matches:
        indiData = match.xpath('.//dd')
        parsedData = []
        for field in indiData:
            parsedData.append(''.join(map(str, field.xpath('.//text()'))))
        for i,x in enumerate(parsedData):
            parsedData[i] = x.strip()
            if x == 'v':
                parsedData[i] = '  v  '
        if len(''.join(parsedData)) == 0:
            continue
        if parsedData[0] == '':
            parsedData = parsedData[1:]
        parsedList.append(parsedData)

    maxLen = reduce(max, map(len, parsedList))
    for i,x in enumerate(parsedList):
        parsedList[i] = ['']*(maxLen-len(x)) + x

    maxColLen = [0]*maxLen
    for i in xrange(maxLen):
        maxColLen[i] = reduce(max, map(len, [x[i] for x in parsedList]))
    parsedList = [[x[i].ljust(maxColLen[i]+2) for i in range(maxLen)] for x in parsedList]
    return '\n'.join(map('\t'.join,parsedList))+'\n'

