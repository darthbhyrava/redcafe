# A script to get data from a list of posts on a thread. 
# Let's start with Juan Mata's thread.
from bs4 import BeautifulSoup
import urllib2

proxy = urllib2.ProxyHandler({'http': 'proxy.iiit.ac.in:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

response = urllib2.urlopen('http://www.redcafe.net/threads/juan-mata-2016-17-performances.419643/page-8')
data = response.read()
file = open("mata8.html", 'w')
file.write(data)
file.close()

with open("mata8.html") as fp:
    soup = BeautifulSoup(fp)
towrite = soup.find_all('blockquote')
file = open('blockquotes', 'w')
for i in towrite:
    file.write(i.encode('utf-8')+"\n\n")
file.close()
