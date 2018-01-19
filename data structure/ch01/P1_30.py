def count_div2(n):
    count = 0
    while n >= 2:
        count = count + 1
        n = n / 2.0
    return count

if __name__ == '__main__':
    print(count_div2(20))
