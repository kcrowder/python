#!/usr/bin/python3
#
# date: 12.03.2017
# by: keith crowder
# name: checking_users.py
#
# exercise 5-10
#
current_users = ['Chlordane', 'Spydat3k', 'R3cluse9', 'Joker', 'Keith']
new_users = ['Jim', 'Kim', 'Jacob', 'Susan', 'Matthew', 'Harlan', 'Keith', 'Chlordane']
#
for name in new_users:
    if name in current_users:
        print("You'll need to choose a different username, " + name.lower() + " is already taken.")
    else:
        print("The username: " + name.lower() + " is available.")
#
print("Done.")
# print("You're doing good, kid. Stay Focused!")
#
# end of program
#
