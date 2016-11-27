# A script to get data from a list of posts on a thread. 
# Let's start with Juan Mata's thread.
from bs4 import BeautifulSoup
import urllib2

def remover(el, tag='div', className=''):
    if className:
        for div in el.find_all(tag, { 'class' : className }): 
            div.decompose()
    else:
        for div in el.find_all(tag): 
            div.decompose()

proxy = urllib2.ProxyHandler({'http': 'proxy.iiit.ac.in:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
i = 1
count = 0
response = urllib2.urlopen('http://www.redcafe.net/threads/juan-mata-2015-16-performances.406616/page-{}'.format(i))
data = response.read()
soup = BeautifulSoup(data)
towrite = soup.find_all('blockquote')
file = open('blockquotes', 'w')

for i in towrite:
    remover(i, 'div')
    remover(i, 'br')
    remover(i, 'blockquote', 'twitter-tweet')
    x = i.contents
    s = ''
    for sentence in x:
        s += str(sentence.encode('utf-8'))
    if len(x):
        count += 1
        post = (str(count) + str('~~~') + "\t" + s.strip()).strip() + "\n\n"
        file.write(post)
file.close()