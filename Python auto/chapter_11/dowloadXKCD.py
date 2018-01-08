import requests, os, bs4, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s\
                              - %(message)s')

url = 'http://xkcd.com/1298/'
os.makedirs('xkcd', exist_ok = True)

while not url.endswith('#'):
    # Download the page.
    logging.debug('Downloading page %s ...' % url)
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        logging.debug('Downloading image %s ...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status
        # Save the image to ./xkcd.
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as\
                imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "http://xkcd.com" + prevLink.get('href')

print('Done')
