import json

with open('number.json','r') as fb:
    num=json.load(fb)
    print("I know your favorite number is ",num)
