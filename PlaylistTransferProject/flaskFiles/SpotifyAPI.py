from flask import jsonify
import spotipy

def getSpotifySongs(playlistUrl):

    spotify = spotipy.Spotify() # TODO: need auth with client secret to access the playlists
    # playlistInfo = spotify.playlist_tracks(playlistUrl)
    

    songs_data = []


    songs_data.append({
        "title": "Gangnam Style",
        "artists": {"PSY"}
    })
    songs_data.append({
        "title": "FE!N (feat. Playboi Carti)",
        "artists": {"Travis Scott", "Playboi Carti"}
    })

    return songs_data



# Should return a json of missing songs + artist and if it was successsful (1=good, 0=bad)
# example: {"functionSuccess": 0, "MissingSongs:" missingSongs}
def createPlaylist(jsonNameAndArtists, name, token):
    spotify = spotipy.Spotify() # TODO: auth with client and user secret

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

    return jsonify({"functionSuccess": 1, "missingSongs": missingSongs})



# for testing purposes
# getSpotifySongs("https://open.spotify.com/playlist/4EYl9HFmiXMSAJzLIX3Wx3?si=b9ab3fc310694c48")