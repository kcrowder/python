#!/usr/bin/python3
#
# date: 12.11.2017
# by: keith crowder
# name: restaurant_seating.py
#
# exercise 7-2
#
dinner = input("How many people will be dining with you this evening? ")
dinner = int(dinner)

if dinner <= 8:
    print("Please, be seated!")
else:
    print("You'll have to wait to 40 minutes while we prepare a table for you and your guests.")
#
# end of program
#
