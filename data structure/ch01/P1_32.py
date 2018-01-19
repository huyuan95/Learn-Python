
ch = ''
result = 0
cal = []
op = '+'
while ch != '=':
    ch = input()
    cal.append(ch)

for i in range(len(cal)):
    num = cal.pop(0)
    try:
        num = float(num)
    except ValueError:
        op = num
        if op == '=':
            print(result)
        continue
    if op == '+':
        result = result + num
    elif op == '-':
        result = result - num
    elif op == '*':
        result = result * num
    elif op == '/':
        result = result / num
