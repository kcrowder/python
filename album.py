#!/usr/bin/python3
#
# date: 12.22.2017
# by: keith crowder
# name: album.py
#
# exercise 8-7
#
print("Just a sample of my awesome album collection...")
def make_album(artist_name, album_title, track=''):
    album = {'Artist Name':artist_name, 'Album Title':album_title}
#    proper_name = artist_name + ' ' + album_title
    if track:
        album['track'] = track
    return album
#    return proper_name.title()
#
collection = make_album('photek','modus operandi')
print(collection)
#
collection = make_album('orbital','insides')
print(collection)
#
collection = make_album('the prodigy','fat of the land')
print(collection)
#
collection = make_album('source direct','exorcise the demons',track=9)
print(collection)
# end of program
#
