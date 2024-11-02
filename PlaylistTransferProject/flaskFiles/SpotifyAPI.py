from flask import jsonify
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import spotipy, Creds, os


# Clears the token cache
def clear_token_cache():
    cache_path = ".cache"
    if os.path.exists(cache_path):
        os.remove(cache_path)
        print("Token cache cleared.")
    else:
        print("No token cache found.")
        

# Checks to see if the words contain half of the same words
# TODO: impliment only if needed
# def isSameSong(song1Name, song2Name):
#     song1Words = song1Name.split(" ")
#     song2Words = song2Name.split(" ")

#     if len(song1Words) > len(song1Words):
#         temp = song1Words
#         song1Words = song2Words
#         song2Words = temp

#     numWordsSimilar = 0
#     for word in song1Words:
#         if word in song1Words:
#             numWordsSimilar += 1

#     if numWordsSimilar > len(song1Words):
#         return True
    
#     return False



def getSpotifySongs(playlistUrl):
    client_id, client_secret, _ = Creds.getSpotifyCreds()

    # Use Client Credentials Flow (no user authentication required)
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    playlist_id = playlistUrl.split("/")[-1].split("?")[0]

    # Get the playlist details
    playlist = spotify.playlist(playlist_id=playlist_id)

    songs_data = []
    counter = 0

    # Fetch the first set of tracks
    tracks = playlist['tracks']
    items = tracks['items']

    # Loop through tracks and handle pagination
    while tracks:
        for item in items:
            counter += 1
            track = item['track']
            song_name = track['name']
            artists = [artist["name"] for artist in track["artists"]]

            songs_data.append({
                "title": song_name,
                "artists": artists,
            })

        # Check if there is another page of tracks
        if tracks['next']:
            tracks = spotify.next(tracks)
            items = tracks['items']
        else:
            tracks = None

    # print(f"{counter} songs in playlist {playlist['name']}") TODO: remove line after testing
    return songs_data



# TODO: remove token as input from all function calls
# Should return a json of missing songs + artist and if it was successsful (1=good, 0=bad)
# example: {"functionSuccess": 1, "MissingSongs:" missingSongs} | {"functionSuccess": 0, error: "error description"}
def createPlaylist(NameAndArtists, playlistName): 
    client_id, client_secret, redirect_uri = Creds.getSpotifyCreds()
    scope = 'playlist-modify-public user-library-read'

    sp_oauth = SpotifyOAuth(client_id=client_id, 
                            client_secret=client_secret,
                            redirect_uri=redirect_uri, 
                            scope=scope)

    token_info = sp_oauth.get_access_token(as_dict=False)

    sp = spotipy.Spotify(auth=token_info)

    user_profile = sp.me()

    playlist = sp.user_playlist_create(user=user_profile['id'], name=playlistName)

    missingSongs = []
    song_uris = []

    for song in NameAndArtists:
        query = f"{song['title']} {song['artists']}"
        result = sp.search(q=query, type='track', limit=1)
        
        if result['tracks']['items']:
            track_uri = result['tracks']['items'][0]['uri']
            song_uris.append(track_uri)
        else:
            missingSongs.append(song)


    if song_uris:
        sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)

    print(f"{user_profile['type']}: {user_profile['display_name']} created playlist: {playlistName}")
    
    clear_token_cache()
    # return jsonify({"functionSuccess": 1, "missingSongs": missingSongs})
    print(missingSongs)



# for testing purposes
# getSpotifySongs("https://open.spotify.com/playlist/4EYl9HFmiXMSAJzLIX3Wx3?si=b9ab3fc310694c48"
# createPlaylist("", "", "")

# getSpotifySongs("https://open.spotify.com/playlist/6v8okK8zzs0UXxBX90ecqB")
# getSpotifySongs("https://open.spotify.com/playlist/4EYl9HFmiXMSAJzLIX3Wx3")

# Testing adding a song (odd results, should try to improve)
# song_info = []
# song_info.append({
#     "title": "Fein",
#     "artists": "Weezer",
# })
# createPlaylist(song_info, "weezed", "")