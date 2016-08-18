#mapit.py
#7/5/16

"""Launches a map in the browser using an address from the command line of
the terminal"""

#The program can be set to open a web browser to 'https://www.google.com/maps/place/your_address_string'
#(where your_address_string is the address you want to map)


import webbrowser

address = raw_input('Enter an address: ')

to_open = 'https://www.google.com/maps/place/'+address

webbrowser.open(to_open)


#Open a second webpage
#address2 = raw_input('Enter another address: ')
#to_open2 = 'https://www.google.com/maps/place/'+address2
#webbrowser.open(to_open2)