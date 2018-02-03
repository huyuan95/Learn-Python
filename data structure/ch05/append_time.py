from time import time
def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.insert(n // 2, None)
    end = time()
    return (end - start) / n

if __name__ == '__main__':
    for i in [100, 1000, 10000, 100000, 1000000, 10000000, 100000000]:
        print(i, compute_average(i))
