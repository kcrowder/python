#!/usr/bin/python3
#
# date: 12.26.2017
# by: keith crowder
# name: magicians.v2.py
#
# exercise 8-10, 8-9 hacked
#
#
def show_magicians(magicians):
    for magician in magicians:
            print(magician.title())

def make_great(magicians):
#
    great_magicians = []
#
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great!"
        great_magicians.append(great_magician)
#
    for great_magician in great_magicians:
        magicians.append(great_magician)
#
magicians = ['bob', 'bill','brenda']
show_magicians(magicians)
#
make_great(magicians)
show_magicians(magicians)
#
# end of program
#
