#!/usr/bin/python3
#
# date: 12.12.2017
# by: keith crowder
# name: multiples_of_ten.py
#
# exercise 7-3
#
number = input("Enter a number: ")
number = int(number)
#
if number % 10 == 0:
    print("\nThe number " + str(number) + " is a multiple of ten.")
else:
    print("\nThe number " + str(number) + " is not a multiple of ten.")
#
# end of program
#
