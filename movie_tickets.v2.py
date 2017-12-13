#!/usr/bin/python3
#
# date: 12.12.2017
# by: keith crowder
# name: movie_tickets.v2.py
#
# exercise 7-6, 7-5 hacked
#
prompt = "\nEnter the age of the child you want to buy a ticket for."
prompt += "\n(The older than child, the more you'll have to pay.) \n"
#
#
age = int(input(prompt))
active = True
while active:
    if age < 3:
        print("Daaaw, so cute. " + str(age) + " year old babies get in for free!")
        active = False
    elif age >= 3 and age <= 12:
        print("The price is $10 for " + str(age) + " year old children.")
        active = False
    elif age > 12:
        print("The price for any one " + str(age) + " years old and older is $15.")
        active = False
#
print("Enjoy the movie!")
#
# end of program
#
