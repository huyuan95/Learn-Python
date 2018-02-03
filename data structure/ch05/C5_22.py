from time import time

with open('RomeoandJuliet.txt', 'r') as f:
    s = f.read()

s = s * 100

temp = []
for ch in s:
    temp.append(ch)

start = time()
temp1 = temp.extend(temp)
end = time()
print('Extend method, elapsed time is {0}'.format(end - start))

temp2 = temp.copy()
start = time()
for ch in temp:
    temp2.append(ch)
end = time()
print('Append method, elapsed time is {0}'.format(end - start))
