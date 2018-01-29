def min_max(data, len, min, max):
    if len == 0:
        return (min, max)
    else:
        len = len -1
        if min > data[len]:
            min = data[len]
        if max < data[len]:
            max = data[len]
        return min_max(data[0: len], len, min, max)

if __name__ == '__main__':
    data = [11,2,4,5,6,7,9,-4]
    min = 10000
    max = -10000
    len = len(data)
    print(min_max(data, len, min, max))
