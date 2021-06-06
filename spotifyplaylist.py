
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
scope = 'playlist-modify-public'
username = 'TO BE FIGURED'

token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

#create the playlist
playlist_name = input("Enter the desired playlist name:")
playlist_description = input("Enter the playlist description:")

spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)


user_input = input('Enter song name or type "quit" to exit:')
list_of_songs = []

while user_input != 'quit':
	result = spotifyObject.search(q=user_input)
	#print(json.dumps(result,sort_keys=4,indent=4))
	list_of_songs.append(result['tracks']['items'][0]['uri'])
	user_input = input('Enter song name or type "quit" to exit:')
	
	#find new playlist
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']
#addsongs
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)
