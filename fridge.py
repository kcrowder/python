#!/usr/bin/python
#
# date: 01.10.2012
# by: keith crowder
# what_the_kcuf: conditionals
# source: inspired by facebook
#
print 'if you want to give up, just type: "give up" '		# instructions
print 'open fridge, to check the fridge'
print 'to look in the pantry, type: "open pantry" '
print 'if you are still hungry, type: "still hungry" '
print 'not hungry, type: "give up" '
#
while True:
	standards = raw_input('enter text: ')

	if standards == 'give up':				# just in case you decided to, uh, give up
		print "that's why, coffee"
		break
	elif standards == 'open fridge':			# anything in the fridge?		
		print 'nothing to eat.'
	elif standards == 'open pantry':			# anything in the pantry?
		print 'nothing to eat.'
#	elif standards.isdigit():
#		print 'Bad!' * 8
	elif standards == 'still hungry':			# you still hungry, repeat
		print 'lower standards and repeat.'
	else: 
		print 'what the...?'				# are you even going to look in a logical place?
		print 
		break
#
# end of program
#
