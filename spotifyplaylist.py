# nicsspotifyplaylistadder
#et directory to nicsvfree
#(cd nicsvfree)
#create virtual env 
#(py -m venv nicspotifyapp)
#nicspotifyapp\Script\activate

#setvariables on command prompt
#set SPOTIPY_CLIENT_ID=06db49bf2c40470ea02d5f8886aa73c6

#set SPOTIPY_CLIENT_SECRET=b5118d429f694e878803d6393507c8f9


#set SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080/

#run via command prompt

#python3 spotifyplaylist.py




import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
scope = 'playlist-modify-public'
username = 'iz6wb3jz8sf98gch08ef1q3jg'

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
