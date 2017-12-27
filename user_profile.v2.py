#!/usr/bin/python3
#
# date: 12.27.2017
# by: keith crowder
# name: user_profile.v2.py
# edited to use my info and title()
# exercise 8-13
#
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('keith', 'crowder',
                             location='dallas',
                             field='information technology',
                             hobbies='cyberpunk')
print(user_profile)
#
# end of program
#
