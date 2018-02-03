from time import time

start = time()
temp = [None] * 1000000
end = time()
print('Comprehensive construct a list, elapsed time is {0}'.format(start -
                                                                   end))
temp = []
start = time()
for i in range(1000000):
    temp.append(None)
end = time()
print('Append construct a list, elapsed time is {0}'.format(start - end))
