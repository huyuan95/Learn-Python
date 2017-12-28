name = input("Input name:")
with open('guest.txt','w') as f:
    f.write(name)
