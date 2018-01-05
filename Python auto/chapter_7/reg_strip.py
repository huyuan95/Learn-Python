import re

def RegStrip(str, ch = ''):
    if ch == '':
        pattern = re.compile(r'^\s*(\S(.*)?\S)\s*$')
        m = re.search(pattern, str)
        return m.group(1)
    else:
        pattern = re.compile(ch)
        return pattern.sub('', str)

word = input("input some words: ")
ch = input('input deleted character: ')

s = RegStrip(word, ch)
print(s)
