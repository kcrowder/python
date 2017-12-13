#!/usr/bin/python3
#
# date: 12.10.2017
# by: keith crowder
# name: fav_numbers.v2.py
#
# exercise 6-10, 6-2 hacked
#
fav_numbers = {
    'keith': ['2501','9000'],
    'kim': ['2600','11'],
    'spydat3k': ['2902','100'],
    'chlordane': ['1981','1989'],
    'joker': ['666','777'],
}
for name, number in fav_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are: ")
    for number in number:
        print("\t" + str(number))
#
# end of program
#
