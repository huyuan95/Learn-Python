import json

num=float(input("Input your favorite number: "))
with open('number.json','w') as fb:
    json.dump(num,fb)
