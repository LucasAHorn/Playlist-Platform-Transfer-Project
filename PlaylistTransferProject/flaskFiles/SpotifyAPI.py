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



def getSpotifySongs(playlistUrl):

    client_id, client_secret, _ = Creds.getSpotifyCreds()

    # Use Client Credentials Flow (no user authentication required)
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    playlist_id = playlistUrl.split("/")[-1].split("?")[0]

    playlist = spotify.playlist(playlist_id=playlist_id)

    songs_data = []

    # Loop through the tracks in the playlist
    for item in playlist['tracks']['items']:
        track = item['track']
        song_name = track['name']  # Get the song name
        artists = [artist["name"] for artist in track["artists"]]

        songs_data.append({
            "title": song_name,
            "artists": artists,
        })
    

    #issue with jsonifying
    print(songs_data)

    return songs_data


# TODO: remove token as input from all function calls
# Should return a json of missing songs + artist and if it was successsful (1=good, 0=bad)
# example: {"functionSuccess": 1, "MissingSongs:" missingSongs} | {"functionSuccess": 0, error: "error description"}
def createPlaylist(jsonNameAndArtists, playlistName, token):


    
    client_id, client_secret, redirect_uri = Creds.getSpotifyCreds()
    scope = 'user-library-read'

    # Authenticate and get token using OAuth
    sp_oauth = SpotifyOAuth(client_id=client_id, 
                            client_secret=client_secret,
                            redirect_uri=redirect_uri, 
                            scope=scope)

    # Get access token
    token_info = sp_oauth.get_access_token(as_dict=False)

    sp = spotipy.Spotify(auth=token_info)

    # Example API call: Get the current user’s profile
    user_profile = sp.me()
    # print(user_profile)
    print(user_profile['type'] + ': ' + user_profile['display_name'] + ' created playlist: ' + playlistName)

    # spotify = spotipy.Spotify() # TODO: auth with client and user secret

    #  Below this just returns
    missingSongs = []

    # testing return values
    missingSongs.append({
        "title": "Gangnam Style",
        "artists": ["PSY"]
    })
    missingSongs.append({
        "title": "FE!N (feat. Playboi Carti)",
        "artists": ["Travis Scott", "Playboi Carti"]
    })

    clear_token_cache()
    return jsonify({"functionSuccess": 1, "missingSongs": missingSongs})



# for testing purposes
# getSpotifySongs("https://open.spotify.com/playlist/4EYl9HFmiXMSAJzLIX3Wx3?si=b9ab3fc310694c48"
# createPlaylist("", "", "")

getSpotifySongs("https://open.spotify.com/playlist/6v8okK8zzs0UXxBX90ecqB")