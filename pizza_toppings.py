#!/usr/bin/python3
#
# date: 12.12.2017
# by: keith crowder
# name: pizza_toppings.py
#
# exercise 7-4, 7-6
#
prompt = "\nPlease enter the toppings you would like on your pizza:"
prompt += "\nEnter 'quit' when you are ready for pizza! "
#
while True:
    topping = input(prompt)

    if topping == 'quit':
        print("We're done here.")
        break
    else:
        print("OK, we'll add " + topping + "!")
#
# end of program
#
