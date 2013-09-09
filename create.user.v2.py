#!/usr/bin/python
#
# by: keith crowder
# date: 01.01.2012
# notes: learning to create a user, os.system, crypt, added while statement
# source(s): http://shutupsquare.wordpress.com/2011/02/13/how-to-use-python-script-to-add-users-to-linux-machine-with-useradd-including-password/; 
# http://www.daniweb.com/software-development/python/threads/253341
# python_version: Python 2.6.6, Python 2.7.0+
#
#
import os, crypt
import time														# added time.sleep 05.05.2013
#
print "we're creating a user, using python..."										# greeting
time.sleep(5)														# sleep five seconds
#
username = raw_input('enter username: ')										# username
while username == 'chlordane':		 					 					# make sure its not 'chlordane'
	print "you can't use chlordane!"
	break
else:
	print "continue..."
	password = raw_input('enter password: ')									# users password
	realname = raw_input('enter realname: ')									# real name of the user
#
##############################
#
	encPass = crypt.crypt(password, "22")										# the password creation
#
	os.system("sudo /usr/sbin/useradd -m -s /bin/bash -p "+encPass+" -c '%s' %s" %(realname, username))		# create userthe useradd one-liner
	# -c 'Real Name'
	os.system("id %s\n" %(username))										# verify uid/gid
	os.system("ls -d /home/%s\n" %(username))									# verify user home
	os.system("finger %s\n" %(username))										# verify finger details
	print "ok, we're done, user %s created" %username
#
time.sleep(5)														
print "see you space cowboy..."
#
# end of program
#
