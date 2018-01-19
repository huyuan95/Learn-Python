def sum_square(n):
    sum = 0
    for i in range(n):
        sum = sum + i ** 2
    return sum

print(sum_square(10))
