#!/usr/bin/python3
#
# date: 12.07.2017
# by: keith crowder
# name: fav_places.py
#
# exercise 6-7, 6-1 hacked
#
people = {
    'kgcrowder': {
        'first_name': 'kim',
        'last_name': 'crowder',
        'favorite_place': 'japan',
        },
    'klcrowder': {
        'first_name': 'keith',
        'last_name': 'crowder',
        'favorite_place': 'hawaii',
        },
    'chlordane': {
        'first_name': 'chlordane',
        'last_name': '(no last name)',
        'favorite_place': 'the net',
        },
}
#
for user, info in people.items():
    print("Username: " + user)
    full_name = info['first_name'] + " " + info['last_name']
    location = info['favorite_place']

    print("\tFull Name: " + full_name.title())
    print("\tFavorite Place: " + location.title())

#
# end of program
#
