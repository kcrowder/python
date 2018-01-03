#!/usr/bin/python3
#
# date: 01/02/2018
# by: keith crowder
# name: users.py
# 9-3: Users
#
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

eric = User('keith', 'crowder', 'keith', 'keith@example.com', 'texas')
eric.describe_user()
eric.greet_user()

willie = User('hacker', 'krolden', 'chlordane', 'chlordane@example.com', 'the net')
willie.describe_user()
willie.greet_user()
#
# end of program
#
