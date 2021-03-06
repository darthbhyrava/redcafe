# A script to get the contents of all the posts in a thread from the RedCafe forum.
# Change the URLs, output file names and page numbers as required (see ./URLs/url_list_players.txt).
#
# Sriharsh Bhyravajjula, 2016

from bs4 import BeautifulSoup
import urllib2

# Method to remove unwanted data.
def remover(el, tag='div', className=''):
    if className:
        for div in el.find_all(tag, { 'class' : className }): 
            div.decompose()
    else:
        for div in el.find_all(tag): 
            div.decompose()

# Change proxy settings as fit.
proxy = urllib2.ProxyHandler({'http': 'proxy.iiit.ac.in:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

# Change pages according to player
pages = 160
count = 0

# Change Output Filename according to player
file = open('wayne_rooney_14-15', 'a+')

for i in range(pages):
    page = i+1
    # Change URL according to player
    url = 'http://www.redcafe.net/threads/wayne-rooney-2014-15-performances.393849/page-%s' % (page)
    print "Getting Data .................................................. %s/%s pages scraped." % (page, pages)
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