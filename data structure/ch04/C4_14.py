def hanoi(n, a, b, c):
    if n == 0:
        return
    else:
        hanoi(n-1, a, c, b)
        print(a, '->', c)
        hanoi(n-1, b, a, c)

if __name__ == '__main__':
    hanoi(7, 'a', 'b', 'c')
