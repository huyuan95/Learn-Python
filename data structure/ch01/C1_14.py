def pair_odd(data):
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i] * data[j] % 2 == 1:
                return True
    return False


if __name__ == '__main__':
    print(pair_odd([1,2,3,4,6]))
