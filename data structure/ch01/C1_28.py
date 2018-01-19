def norm(v, p = 2):
    sum = 0
    for i in v:
        sum = sum + i**p
    return sum**(1/p)

if __name__ == '__main__':
    print(norm([3,4],4))
