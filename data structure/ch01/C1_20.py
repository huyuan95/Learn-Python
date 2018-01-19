import random

def own_shuffle(data):
    result = []
    while data != []:
        i = random.randint(0, len(data)-1)
        result.append(data.pop(i))
    return result

if __name__ == '__main__':
    print(own_shuffle([2,3,4,5,6]))
