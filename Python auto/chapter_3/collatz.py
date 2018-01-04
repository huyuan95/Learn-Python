def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3*num + 1

try:
    number = int(input('Input a number: '))
except ValueError:
    print('Please input an integer')
else:
    while number != 1:
        number = collatz(number)
        print(number)
