import re

pwd = input('Inpur Password :')

if len(pwd) >= 8 and re.search(r'[a-z]', pwd) and re.search(r'[A-Z]', pwd) and\
        re.search(r'[0-9]', pwd):
    print("good password")
else:
    print('password need contain at least one lower character, one upper '
          'character, one digit')
