from time import time

with open('RomeoandJuliet.txt', 'r') as f:
    s = f.read()

s = s * 100

start = time()
letters = ''
for ch in s:
    if ch.isalpha():
        letters += ch
end = time()
print('Method 1, elapsed time is {0}'.format(end - start))

start = time()
temp = []
for ch in s:
    if ch.isalpha():
        temp.append(ch)
end = time()
print('Method 2, elapsed time is {0}'.format(end - start))

start = time()
letters = ''.join([ch for ch in s if ch.isalpha()])
end = time()
print('Method 3, elapsed time is {0}'.format(end - start))

start = time()
letters = ''.join(ch for ch in s if ch.isalpha())
end = time()
print('Method 4, elapsed time is {0}'.format(end - start))
