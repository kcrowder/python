#!/usr/bin/python3
#
# date: 12.05.2017
# by: keith crowder
# name: glossary.v2.py
#
# exercise 6-4
#
#
glossary = {
    'variables':'hold a value.',
    'strings':'are a series of numbers.',
    'integers':'are numbers without a decimal point.',
    'floats':'are numbers with a decimal point.',
    'comments':'are internal notes on code written.',
    'lists':'are a collection of items in a particular order.',
    'elements':'can be found in lists.',
    'pop':'method for removing the last item in a list',
    'insert':'adds new elements at any position in your list',
    'del':'will delete an item from a list',
    'remove':'allows for removing an item from a list',
}
#
for key, value in glossary.items():
    print("Key: " + key)
    print("Value: " + value + "\n")
#
# end of program
#
