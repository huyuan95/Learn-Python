def minmax(numbers):
    max = 0
    min = 0
    if isinstance(numbers, (int, float)):
        max = min = numbers
        return (min, max)
    for i in range(len(numbers)):
        if i == 0:
            max = numbers[i]
            min = numbers[i]
        else:
            if numbers[i] > max:
                max = numbers[i]
            if numbers[i] < min:
                min = numbers[i]
    return (min, max)

print(minmax([-1, 3, -4, 5.6]))
