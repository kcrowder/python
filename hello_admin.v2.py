#!/usr/bin/python3
#
# date: 11.30.2017
# by: keith crowder
# name: hello_admin.v2.py
#
# exercise 5-9
#
#usernames = ['keith', 'tom', 'bob', 'eric', 'will', 'admin']    # random names plus admin
usernames = []    # empty list
#
if usernames:
    for name in usernames:
        print("Hello ," + name + "would you like to see a status report.")
    print("Looks like no body is home.")
else:
    print("You have to be a valid user to access this system")

# print("You're doing good, kid. Stay Focused!")
#
# end of program
#
