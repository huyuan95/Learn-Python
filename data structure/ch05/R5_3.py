import sys
data = [None]*10000
cur = sys.getsizeof(data)
print('Length: {0:3d}; Size in bytes: {1:4d}'.format(len(data), cur))
for k in range(len(data)):
    a = len(data)
    b = sys.getsizeof(data)
    if b != cur:
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        cur = b
    data.pop()
