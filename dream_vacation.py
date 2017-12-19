#!/usr/bin/python3
#
# date: 12.14.2017
# by: keith crowder
# name: dream_vacation.py
#
# exercise 7-10
#
prompt = "\nIf you could visit any place in the world, where would it be?"
prompt += "\nTell us below. Type 'quit' when you are done: "
#
while True:
    dream = input(prompt)

    if dream == 'quit':
        break
    else:
        print("I'd love to go to " + dream.title() + "!")
#
# end of program
#
