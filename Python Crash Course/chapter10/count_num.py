# -*- coding: utf-8 -*-

with open('david.txt','r') as fb:
    txt=fb.read().decode('utf-8')
    num=txt.lower().count('the')
    print('"The" appears %d times in "David Copperfield"')
