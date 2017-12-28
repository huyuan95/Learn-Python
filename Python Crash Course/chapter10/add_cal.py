try:
    a = float(input('Input a number: '))
    b = float(input('Input a number: '))
except ValueError:
    print('Two number needed.')
else:
    print(a+b)
