#! /Users/dreamyang/anaconda3/bin/python

import webbrowser, sys, pyperclip

print(sys.argv)
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('http://map.google.com/maps/place/' + address)
