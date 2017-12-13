#!/usr/bin/python3
#
# date: 12.10.2017
# by: keith crowder
# name: cities.py
#
# exercise 6-11
#
cities = {
    'tokyo': {
        'country':'japan',
        'population':'9.273',
        'fact':'At over 5,000 square miles, the Greater Tokyo Area is the second largest metropolitan area on the planet in terms of urban landmass.\n',
        },
    'kailua': {
        'country':'united states',
        'population':'38,635',
        'fact':'In the Hawaiian language Kailua means "two seas," or "two currents," a contraction of the words kai (meaning sea or sea water) and ʻelua (meaning two); '
        'it is so named because of the two lagoons in the district or the two currents which run through Kailua Bay.\n',
        },
    'london': {
        'country':'england',
        'population':'8.788',
        'fact':'The London Underground is the oldest underground railway network in the world.\n',
        },
}
#
for city, data in cities.items():
    print("City: " + city)
    where = data['country']
    people =  data['population']
    trivia = data['fact']

    print("\tCountry: " + where.title())
    print("\tPopulation: " + str(people))
    print("\tFun Fact: " + trivia)

#
# end of program
#
