#! /Users/dreamyang/anaconda3/bin/python
import requests, sys, webbrowser, bs4, logging
logging.disable(logging.DEBUG)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s\
                              - %(message)s')
logging.debug("Program start")
print('Googling...')
res = requests.get('http://baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.t a')
logging.debug(linkElems)
numOpen = min(5, len(linkElems))
logging.debug(str(numOpen))
for i in range(numOpen):
    logging.debug(linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))
