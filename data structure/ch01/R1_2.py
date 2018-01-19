def is_even(k):
    k=abs(k)
    for i in range(k+1):
        if k == 0:
            return True
        elif k == 1 or k == -1:
            return False
        k = k - 2

print(is_even(4))
