import os
import requests
import pandas as pd

PATH = r'/Users/dreamyang/Desktop/iris/'

r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
with open(PATH + 'iris.data', 'w') as f:
    f.write(r.text)
    
os.chdir(PATH)

df = pd.read_csv(PATH + 'iris.data', names = ['sepal length', 'sepal width',
                                              'petal length', 'petal width',
                                              'class'])
df.head()
print(df['sepal length'])
