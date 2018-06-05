import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

def setup_data(public_id,secret_id):
    """Creates the spotipy object in order to use the sopotify developer's API """
    client_credentials_manager = SpotifyClientCredentials(client_id=public_id,client_secret=secret_id)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def top2_tracs(band_Uri, sp):
    """Returns a list containing the two most famous tracks of the band_Uri"""
    tracks = []
    results = sp.artist_top_tracks(band_Uri)
    for track in results['tracks'][:2]:
        tracks.append(track['name'])
    return tracks

def band_genres(band_Uri, sp):
    """Returns a list containing the genres of the band_Uri"""
    results = sp.artist(band_Uri)
    return results['genres']

def band_name(band_Uri, sp):
    """Returns the band_Uri name"""
    results = sp.artist(band_Uri)
    return results['name']

def related_artists(band_Uri, sp):
    results = sp.artist_related_artists(band_Uri)
    """Returns a list containing the two most related artists of band_Uri"""
    artistList = []
    for artist in results['artists'][:2]:
        artistList.append(artist['name'])
    return artistList
