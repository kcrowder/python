#!/usr/bin/python3
#
# date: 11.30.2017
# by: keith crowder
# name: hello_admin.py
#
# exercise 5-8
#
usernames = ['keith', 'tom', 'bob', 'eric', 'will', 'admin']    # random names plus admin
#
for name in usernames:
    if name == 'admin':
        print("Hello Admin, would you like to see a status report.")
    elif name == 'eric':
        print("Hello Eric, thank you for logging in again.")
    elif name == 'tom':
        print("Hello Tom, thank you for logging in again.")
    elif name == 'bob':
        print ("Hello Bob, thank you for logging in again.")
    elif name == 'will':
        print("Hello Will, thank you for logging in again.")
    elif name == 'keith':
        print("Hello Keith, thank you for logging in again.")

print("You're doing good, kid. Stay Focused!")
#
# end of program
#
