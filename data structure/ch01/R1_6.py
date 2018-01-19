def odd_square(n):
    result = 0
    for i in range(n):
        if (i+1) % 2 == 1:
            result = result + (i+1)**2
    return result


if __name__ == '__main__':
    print(odd_square(4))
