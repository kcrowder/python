#!/usr/bin/python3
#
# date: 12.12.2017
# by: keith crowder
# name: no_pastrami.py
#
# exercise 7-9, 7-8 hacked
#
sandwhich_orders = ['chicken','pastrami','tuna','pastrami','salmon','pastrami','brisket','pastrami','turkey']
finished_sandwhiches = []
#
while sandwhich_orders:
        sandwhich = sandwhich_orders.pop()
#
        print("Chiecking the shelf for: " + sandwhich.title())
        print("----------The Sandwhiches----------")
        finished_sandwhiches.append(sandwhich)
#
        print("The following sandwhiches have been made: ")
        while 'pastrami' in finished_sandwhiches:
            finished_sandwhiches.remove('pastrami')
            print("We are all out of pastrami, oops.")
        for sandwhich in finished_sandwhiches:
            print(sandwhich.title())
#
print("------------------------------")
print("Thanks for stopping by!")
#
# end of program
#
