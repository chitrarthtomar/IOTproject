import urllib.request
import time
from xml.dom.minidom import parseString

def news(i):
     file = urllib.request.urlopen('http://feeds.feedburner.com/techcrunch')
     data = file.read()
     file.close()
     dom = parseString(data)
     xmlTag = dom.getElementsByTagName('title')[i+2].toxml()
     xmlData= xmlTag.replace('<title>','').replace('</title>','')
     print (xmlData)
     return (xmlData)

