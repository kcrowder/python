#!/usr/bin/python3
#
# date: 12.18.2017
# by: keith crowder
# name: tshirt.v2.py
#
# exercise 8-4, 8-3 hacked
#
print("\n")
def make_shirt(size, text):
    if size == 'large':
        print("I love Python!")
        print("The text on the shirt is: " + text + ".\n")
    elif size == 'medium':
        print ( size.title() + "...you have chosen wisely.")
        print("The text on the shirt is: " + text + ".\n")
    else:
        print("You've chosen a non-standard size of " + size.title())
        print("The text on the shirt is: " + text + ".\n")
#    print("\n")
#
#print("Enjoy!")
make_shirt('small','Whatcha talkin about Willis?')
make_shirt('medium','Whatcha talkin about Willis?')
make_shirt('large','Whatcha talkin about Willis?')
make_shirt('extra large','Whatcha talkin about Willis?')
make_shirt('extra extra large','Whatcha talkin about Willis?')
#
#
# end of program
#
