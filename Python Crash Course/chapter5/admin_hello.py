name_list=()
if name_list:
    for name in name_list:
        if name == 'admin':
            print('Hello admin, would you like to see the status report?')
        else:
            print('Hello %s, thank you for logging again' % name)
else:
    print('We need to find some users')
