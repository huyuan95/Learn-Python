#! /Users/dreamyang/anaconda3/bin/python
import requests, sys, webbrowser, bs4, logging, urllib

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s\
                              - %(message)s')
logging.debug("Program start")
print('Googling...')
# res = urllib.request.urlopen(r'https://google.com/search?q=fly').read()
res = requests.get('http://bing.com/search?q=' + ' '.join(sys.argv[1:]))
# res = requests.get('http://python.org')
res.raise_for_status()
soup = bs4.BeautifulSoup(res)

linkElems = soup.find_all('.r a')
logging.debug(linkElems)
numOpen = min(5, len(linkElems))
logging.debug(str(numOpen))
for i in range(numOpen):
    logging.debug(linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))
