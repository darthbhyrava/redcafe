# Sriharsh Bhyravajjula, 2016 (Gandalf Greyhame)
# A script to get the contents of all the posts in a thread from redcafe.net
# Change the URLs and page as required (see ./URLs/url_list_players.txt)

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

# Change pages according to player
pages = 12
count = 0
# Change Output Filename according to player
file = open('james_wilson_15-16', 'a+')
for i in range(pages):
    page = i+1
    # Change URL according to player
    url = 'http://www.redcafe.net/threads/james-wilson-2015-16-performances.406636/page-%s' % (page)
    print "Getting Data ..........  %s/%s pages scraped." % (page, pages)
    response = urllib2.urlopen(url)
    data = response.read()
    thread = BeautifulSoup(data)
    towrite = thread.find_all('blockquote')
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
            post = (str(count) + str('~~~') + "\n" + s.strip()).strip() + "\n\n"
            file.write(post)
print "Done!"
file.close()