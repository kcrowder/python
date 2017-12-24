#!/usr/bin/python3
#
# date: 12.21.2017
# by: keith crowder
# name: cities.names.py
#
# exercise 8-6
#
def city_country(city,country):
    print("\nShow me the city and country of origin.")
    locations = city + ', ' + country
    return locations.title()

places = city_country('dallas','united states')
print(places)
places = city_country('london','england')
print(places)
places = city_country('tokyo','japan')
print(places)
#
# end of program
#
