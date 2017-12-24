#!/usr/bin/python3
#
# date: 12.23.2017
# by: keith crowder
# name: album.v2.py
#
# exercise 8-8, 8-7 hacked
#
print("Just a sample of my awesome album collection...")
#def make_album(artist_name, album_title, track=''):
def make_album(artist_name, album_title):
    album = {'Artist Name':artist_name.title(), 'Album Title':album_title.title()}
    return album

while True:
    print("\nPlease enter the artist name and album title: ")
    print("(enter 'q' to quit at anytime)")

    a_name = input("Artist Name: ")
    if a_name == 'q':
        break

    a_title = input("Album Title: ")
    if a_title == 'q':
        break
    collection = make_album(a_name, a_title)
    print(collection)
#
# end of program
#
