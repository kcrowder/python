#!/usr/bin/python3
#
# date: 12.10.2017
# by: keith crowder
# name: pets.py
#
# exercise 6-8
#
pets = {
    'yoshi': {
        'first_name': 'kim',
        'last_name': 'crowder',
        'pet_type':'cat'
        },
    'salty': {
        'first_name': 'keith',
        'last_name': 'crowder',
        'pet_type':'dog'
        },
    'kojima': {
        'first_name': 'spyda',
        'last_name': 't3k',
        'pet_type': 'snake',
        },
}
#
for user, info in pets.items():
    print("Username: " + user.title())
    full_name = info['first_name'] + " " + info['last_name']
    animal = info['pet_type']

    print("\tOwner's Name: " + full_name.title())
    print("\tPet Type: " + animal.title())
#
# end of program
#
