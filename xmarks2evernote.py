#POST to each URL
#https://www.evernote.com/clip.action?url=http://contellio.com/resources/evernote-list.html&title=Top+7+Effortless+Ways+to+Convert+Your+Blog+Posts+to+Other+Formats
from lxml import html
#change the filename listed below to your filename
f = open('~/xmarks-bookmarks-2015-12-26.html')
st = f.read()
tree = html.fromstring(st)
#select all of the href's and the text note with the bookmark
urls = tree.xpath('//a/@href')
title = tree.xpath('//a/text()')
#these numbers should match
print len(urls)
print len(title)
#zip them together into a pair inside of a list
notes= (map(list,zip(urls,title)))
from time import sleep
import urllib2
import selenium.webdriver as webdriver
#This is the format of the evernote web request.
#f = urllib.urlopen("https://www.evernote.com/clip.action?url=http://contellio.com/resources/evernote-list.html&title=Top+7+Effortless+Ways+to+Convert+Your+Blog+Posts+to+Other+Formats")
#url=http://contellio.com/resources/evernote-list.html
#&title=Top+7+Effortless+Ways+to+Convert+Your+Blog+Posts+to+Other+Formats'
#Use selenium test suite to open Firefox window so that the tab can be re-used and we don't use potentially thousands of tabs!
b = webdriver.Firefox()
for idx,note in enumerate(notes):
    #Check the URL - maybe it relates to a location that is not so good anymore?
    result = urllib2.urlopen(note[0])
    try:
        result.read()
    except urllib2.HTTPError:
        print note[0]
        continue
    noteurl = 'url=%s' % note[0]
    title = '&title=%s' % urllib.quote_plus(note[1].encode('ascii','ignore'))
    url = 'https://www.evernote.com/clip.action?' + noteurl + title
    print idx
    #print url
    b.get(url)
    sleep(20)
