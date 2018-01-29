def subset(a, n):
    if n == 0:
        return []
    else:
        print([a[0]] + subset(a[1:], n-1))
        print([]+subset(a[1:],n-1))

subset([1,2,3,4,5], 5)
