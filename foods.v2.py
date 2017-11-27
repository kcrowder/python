#!/usr/bin/python3
#
# date: 11.26.2017
# by: keith crowder
#
# 4-10 slicing
#
my_foods = ['pizza', 'falafel', 'carrot cake', 'chicken', 'waffles', 'salad', 'thai food']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

#print("\n")
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

print("\nThe first three items in the list are: ")
print(my_foods[0:3])

print("\nThe itemns from the middle of the list are: ")
print(my_foods[:])

print("\nThe last three items in the list are: ")
print(my_foods[-3:])
#print("\n")
#
# end of program
#
