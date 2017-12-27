#!/usr/bin/python3
#
# date: 12.27.2017
# by: keith crowder
# name: cars.py
#
# exercise 8-14
# https://ehmatthes.github.io/pcc/solutions/chapter_8.html#8-14-cars
#
def make_car(make, model, **options):
    car = {}
    car['Make'] = make.title()
    car['Model'] = model.title()
    for option, value in options.items():
        car[option] = value
    return car
#
old_audi = make_car('audi','a4',
                    color='black',
                    year='2010',
                    transmission='automatic')
new_vw = make_car('vw','gti',
                    color='dark grey',
                    year='2016',
                    transmission='dsg')
print(old_audi)
print(new_vw)
#
# end of program
#
