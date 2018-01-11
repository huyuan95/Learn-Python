import pandas as pd
import numpy as np
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

url="https://www.google.com/flights/explore/#explore;f=JFK,EWR,LGA;t=HND,NRT,TPE,HKG,KIX;li=8;lx=14;d=2018-02-01"

options = Options()
options.add_argument('-headless')
driver = Firefox(executable_path='/Users/dreamyang/Downloads/geckodriver', firefox_options=options)
wait = WebDriverWait(driver, timeout=10)
driver.get(url)
driver.save_screenshot(r'flight_explorer.png')
time.sleep(20)

s = BeautifulSoup(driver.page_source, 'lxml')
best_price_tags = s.find_all('span', 'CTPFVNB-v-k')
best_prices = []
for tag in best_price_tags:
    best_prices.append(int(tag.text.replace('$', '')))

best_price = best_prices[0]
best_height_tags = s.find_all('div', 'CTPFVNB-w-x CTPFVNB-w-f')
best_heights = []
for t in best_height_tags:
    best_heights.append(float(t.attrs['style'].split('height: ')[1].replace('px;', '')))
best_height = best_heights[0]

pph = np.array(best_price) / np.array(best_height)

cities = s.findAll('div', 'CTPFVNB-v-d')

hlist=[]
for bar in cities[0].findAll('div', 'CTPFVNB-w-x'):
    hlist.append(float(bar['style'].split('height: ')[1].replace('px;', ''))*pph)
fares = pd.DataFrame(hlist, columns = ['price'])

fig, ax = plt.subplots(figsize = (10, 6))
plt.scatter(np.arange(len(fares['price'])), fares['price'])
px = [x for x in fares['price']]
ff = pd.DataFrame(px, columns = ['fares']).reset_index()
X = StandardScaler().fit_transform(ff)
db=DBSCAN(eps=1.5, min_samples=1).fit(X)
labels = db.labels_
clusters = len(set(labels))
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
plt.subplots(figsize=(12,8))
for k,c in zip(unique_labels, colors):
    class_member_mask=(labels==k)
    xy=X[class_member_mask]
    plt.plot(xy[:,0],xy[:,1],'o',markerfacecolor=c,markeredgecolor='k',markersize=14)
plt.title('Total Clusters:{}'.format(clusters),fontsize=14,y=1.01)
pf=pd.concat([ff,pd.DataFrame(db.labels_,columns=['cluster'])],axis=1)
rf=pf.groupby('cluster')['fares'].agg(['min','count'])
driver.quit()

