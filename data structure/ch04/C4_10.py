def int_log2(n):
    if n < 2:
        return 0
    else:
        return 1 + int_log2(n//2)


if __name__ == '__main__':
    print(int_log2(19))
