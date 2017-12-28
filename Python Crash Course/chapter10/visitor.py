name = ''
with open('guest_book.txt','w') as f:
    while name != 'exit':
        name = input('Input Name(exit to stop): ')
        if name != 'exit':
            print('Welcome, %s' % name)
            f.write(name+'\n')
