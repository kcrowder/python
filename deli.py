#!/usr/bin/python3
#
# date: 12.12.2017
# by: keith crowder
# name: deli.py
#
# exercise 7-8
#
sandwhich_orders = ['chicken','tuna','salmon','brisket','turkey']
finished_sandwhiches = []
#
while sandwhich_orders:
        sandwhich = sandwhich_orders.pop()

        print("Chiecking the shelf for: " + sandwhich.title())
        finished_sandwhiches.append(sandwhich)
#
        print("The following sandwhiches have been made: ")
        for sandwhich in finished_sandwhiches:
            print(sandwhich.title())
#
# end of program
#
