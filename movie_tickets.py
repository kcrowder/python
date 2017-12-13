#!/usr/bin/python3
#
# date: 12.12.2017
# by: keith crowder
# name: movie_tickets.py
#
# exercise 7-5
#
prompt = "\nEnter the age of the child you want to buy a ticket for."
prompt += "\n(The older than child, the more you'll have to pay.) \n"
#
# while True:
age = int(input(prompt))
#
#    if age == 'quit':
#        print("It appars we are done here.")
#        break
if age < 3:
    print("Daaaw, so cute. " + str(age) + " year old babies get in for free!")
elif age >= 3 and age <= 12:
    print("The price is $10 for " + str(age) + " year old children.")
elif age > 12:
    print("The price for any one" + str(age) + " years old and older is $15.")
#
print("Enjoy the movie!")
#
# end of program
#
