# Sriharsh Bhyravajjula, 2016 (Gandalf Greyhame)
# A script to get the contents of all the posts in a thread from redcafe.net
# Change the URLs and page as required for the following players:
#
#   2015/16 Season - Manchester United Players
#
#   PLAYER                  URL                                                                                          PAGES
#   Adnan Januzaj           http://www.redcafe.net/threads/adnan-januzaj-2015-16-performances.406662/page-               59
#   Ander Herrera           http://www.redcafe.net/threads/ander-herrera-2015-16-performances.406635/page-               67
#   Andreas Pereira         http://www.redcafe.net/threads/andreas-pereira-2015-16-performances.406742/page-             34
#   Anthony Martial         http://www.redcafe.net/threads/anthony-martial-2015-16-performances.408881/page-             169
#   Antonio Valencia        http://www.redcafe.net/threads/antonio-valencia-2015-16-performances.406884/page-            35
#   Ashley Young            http://www.redcafe.net/threads/ashley-young-2015-16-performances.407139/page-                20
#   Bastian Schweinsteiger  http://www.redcafe.net/threads/bastian-schweinsteiger-2015-16-performances.406429/page-      115
#   Cameron B. Jackson      http://www.redcafe.net/threads/cameron-borthwick-jackson-2015-16-performances.412210/page-   23
#   Chris Smalling          http://www.redcafe.net/threads/chris-smalling-2015-16-performances.406695/page-              67
#   Daley Blind             http://www.redcafe.net/threads/daley-blind-2015-16-performances.406784/page-                 80
#   David de Gea            http://www.redcafe.net/threads/david-de-gea-2015-16-performances.406643/page-                43
#   Donald Love             http://www.redcafe.net/threads/james-wilson-2015-16-performances.406636/page-                2
#   Guillermo Varela        http://www.redcafe.net/threads/guillermo-varela-2015-16-performances.412101/page-            20
#   James Wilson            http://www.redcafe.net/threads/james-wilson-2015-16-performances.406636/page-                12
#   Javier Hernandez        http://www.redcafe.net/threads/javier-hernandez-2015-16-performances.408032/page-            9
#   Jesse Lingard           http://www.redcafe.net/threads/jesse-lingard-2015-16-performances.406791/page-               89
#   Jonny Evans             http://www.redcafe.net/threads/jonny-evans-2015-16-performances.406883/page-                 3
#   Juan Mata               http://www.redcafe.net/threads/juan-mata-2015-16-performances.406616/page-                   104
#   Luke Shaw               http://www.redcafe.net/threads/luke-shaw-2015-16-performances.406519/page-                   28
#   Marcos Rojo             http://www.redcafe.net/threads/marcos-rojo-2015-16-performances.407110/page-                 34
#   Marcus Rashford         http://www.redcafe.net/threads/marcus-rashford-2015-16-performances.415079/page-             53
#   Marouane Fellaini       http://www.redcafe.net/threads/marouane-fellaini-2015-16-performances.406879/page-           107
#   Matteo Darmian          http://www.redcafe.net/threads/matteo-darmian-2015-16-performances.406447/page-              83
#   Memphis Depay           http://www.redcafe.net/threads/memphis-depay-2015-16-performances.406638/page-               190
#   Michael Carrick         http://www.redcafe.net/threads/michael-carrick-2015-16-performances.406783/                  34
#   Morgan Schneiderlin     http://www.redcafe.net/threads/morgan-schneiderlin-2015-16-bench-performances.406512/page-   73
#   Nick Powell             http://www.redcafe.net/threads/nick-powell-2015-16-performances.411284/page-                 8
#   Paddy McNair            http://www.redcafe.net/threads/paddy-mcnair-2015-16-performances.407129/page-                9
#   Phil Jones              http://www.redcafe.net/threads/phil-jones-2015-16-injuries-performances.406785/              24
#   Sergio Romero           http://www.redcafe.net/threads/sergio-romero-2015-16-performances.407172/                    26
#   Timothy Fosu Mensah     http://www.redcafe.net/threads/timothy-fosu-mensah-2015-16-performances.415153/page-         30
#   Tyler Blackett          http://www.redcafe.net/threads/tyler-blackett-2015-16-performances.406782/page-              5
#   Wayne Rooney            http://www.redcafe.net/threads/wayne-rooney-2015-16-performances.406644/page-                334


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
pages = 334
count = 0
# Change Output Filename according to player
file = open('wayne_rooney_15-16', 'a+')
for i in range(pages):
    page = i+1
    # Change URL according to player
    url = 'http://www.redcafe.net/threads/wayne-rooney-2015-16-performances.406644/page-%s' % (page)
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