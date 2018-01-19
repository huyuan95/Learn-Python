lines=[]
try:
    while True:
        lines.append(input('input a line: '))
except EOFError:
    for i in range(len(lines)):
        print(lines[-i-1])
