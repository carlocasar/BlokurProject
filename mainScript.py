import spotipy
import json
import sys
import ast
from BlokurProject import musicColector as ms

def main():
    """ In order, the uris of the next bands: Metallica, led zeppelin, kendric lamar, ed sheeran """
    name_bands = ['spotify:artist:2ye2Wgw4gimLv2eAKyk1NB', 'spotify:artist:36QJpDe2go2KgaRleHCDTp', 'spotify:artist:2YZyLoL8N0Wb9xBt1NhZWg', 'spotify:artist:6eUKZXaKkcviH0Ku9w2n3V' ]

    sp = ms.setup_data("5661f893273a47f7859cf5fc80f77bf6", "3426021191fc4c5baa81e0fec70604e5")
    dict_answer = {}
    dict_answer['artists'] = []
    list_all_genres = []

    """create a dictionarie that contains a list with the next information: Name of the band, genres, top 2 tracks, related artists"""
    for band in name_bands:
        dict_answer['artists'].append({"name":ms.band_name(band, sp), "topTracks":ms.top2_tracs(band,sp), "genres":ms.band_genres(band,sp), "recommendedArtists":ms.related_artists(band,sp)})
        list_all_genres.extend(ms.band_genres(band,sp))
    list_all_genres = list(set(list_all_genres))

    """ First, the program asks for a genre that you like from a list, then selects the artists that has this genre and print his best songs and also some related artists"""
    while(True):
        answer = input("\n\n Write the genre that you are more interested in from the list(without single quotes): " + str(list_all_genres))
        if answer in list_all_genres:
            break
        else:
            print("not a genre on the list, try again!")
    for artist in dict_answer['artists']:
        if answer in artist['genres']:
            print('I highly recommend you to listen to the following songs: ' + artist['topTracks'][0] + " and " + artist['topTracks'][1] + " from " + artist['name'])
            print('Also, if you like these songs, give a try to the following artists: ' + artist['recommendedArtists'][0] + ", " + artist['recommendedArtists'][1])
            break

if __name__ == "__main__":
    main()
