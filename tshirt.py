#!/usr/bin/python3
#
# date: 12.18.2017
# by: keith crowder
# name: tshirt.py
#
# exercise 8-3
#
def make_shirt(size, text):
    print("\nThe size of the shirt is: " + size.title() + ".")
    print("The text on the shirt is: " + text + ".")
#    print("\n")

print("Function called using Positional Arugments: ")
make_shirt('large','Whatcha talkin about Willis?')
#
print("Function called using Keyword Arguments: ")
make_shirt(size='large',text='Whatcha talkin about Willis?')
#
# end of program
#
