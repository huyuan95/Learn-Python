def mul(m, n):
    if n == 1:
        return m
    else:
        return m + mul(m, n-1)
    
if __name__ == '__main__':
    print(mul(5,4))
