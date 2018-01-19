
ch = ''
result = 0
cal = []
op = '+'
while ch != '=':
    ch = input()
    try:
        num = float(ch)
    except ValueError:
        op = ch
        continue
    if op == '+':
        result = result + num
    elif op == '-':
        result = result - num
    elif op == '*':
        result = result * num
    elif op == '/':
        result = result / num
    print(result)
