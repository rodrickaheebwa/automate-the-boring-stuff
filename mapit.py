#! python3
#mapit - launches a map in the browser using an address from the browser or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #get address from command line
    address = '+'.join(sys.argv[1:])
else:
    #get address from clipboard
    address = pyperclip.paste()

address = 'https://www.google.com/maps/place/' + address
webbrowser.open(address)
