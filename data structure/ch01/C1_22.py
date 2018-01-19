def dot_product(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c

if __name__ == '__main__':
    print(dot_product([1,2,3],[3,4,5]))
