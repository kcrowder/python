#!/usr/bin/python3
#
# date: 12.07.2017
# by: keith crowder
# name: person_data.v2.py
#
# exercise 6-7, 6-1 hacked
#
people = {
    'kgcrowder': {
        'first_name': 'kim',
        'last_name': 'crowder',
        'age': '27',
        'city': 'dallas',
        },
    'klcrowder': {
        'first_name': 'keith',
        'last_name': 'crowder',
        'age': '36',
        'city': 'dallas',
        },
    'spydat3k': {
        'first_name': 'spyda',
        'last_name': 't3k',
        'age': '2600',
        'city': 'net',
        },
}
#
for user, info in people.items():
    print("Username: " + user)
    full_name = info['first_name'] + " " + info['last_name']
    how_old =  info['age']
    location = info['city']

    print("\tFull Name: " + full_name.title())
    print("\tAge: " + str(how_old))
    print("\tLocation: " + location.title())

#
# end of program
#
