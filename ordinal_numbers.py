#!/usr/bin/python3
#
# date: 12.03.2017
# by: keith crowder
# name: ordinal_numbers.py
#
# exercise 5-11
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
for number in numbers:
    if number == 1:
        print("1st")               # prints '1st'
    elif number == 2:
        print("2nd")               # prints '2nd'
    elif number == 3:
        print("3rd")               # prints '3rd'
    else:
        print( str(number) + "th") # 4 through 9 will be processed as strings with 'th' appended to the end.
#
print("Ordinal Number run complete.")
#
# end of program
#
