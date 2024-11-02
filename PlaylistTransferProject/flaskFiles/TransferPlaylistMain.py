from flask import Flask, jsonify, request
from flask_cors import CORS
import SpotifyAPI, YTMusicAPI
import random


app = Flask(__name__)
CORS(app)

# Gets data from browser
# Outputs url, name, token
def getData():
        data = request.get_json()
        return data['url'], data['name']


# This will find what the starting platform is
#returns: boolean, songlist
def getSongs(url):
    if(url.find("spotify.com") > -1):
        print("from a spotify playlist")
        return True, SpotifyAPI.getSpotifySongs(url)

    if(url.find("music.youtube.com") > -1):
        print("from a YT music playlist")
        return True, YTMusicAPI.getYTSongs(url)

    return False, ""
    
# Gives an unnamed playlist a name
def giveRandomName():
    return f"RenameMe{random.randint(100000000, 1000000000)}"


# Transfers playlist to Spotify
@app.route('/api/ToSpotify', methods=['POST'])
def YTMusicToSpotify():
    url, name = getData()
    
    try:
        fnSuccess, song_data = getSongs(url)
    except:
        return jsonify({"functionSuccess": 0, "errorMessage": "Error getting songs"})


    if fnSuccess == False:
        return jsonify({"functionSuccess": 0, "errorMessage": "given playlist could not be reached"})
    
    if not name:
        name = giveRandomName()
    
    try:
        missingSongs = SpotifyAPI.createPlaylist(song_data, name)   # TODO: look into this:
                                                                    # HTTP Error for POST to https://api.spotify.com/v1/playlists/1bqCeOySqMaQg3nBom6Lhu/tracks with Params: {'position': None} returned 400 due to Too many ids requested
        return jsonify({"functionSuccess": 1, "missingSongs": "missingSongs", "name": name})
    except:
        return jsonify({"functionSuccess": 0, "errorMessage": "Error creating playlist"})

# Transfers a playlist to YT
@app.route('/api/ToYTMusic', methods=['POST'])
def SpotifyToYTMusic():
    url, name = getData()

    try:
        fnSuccess, song_data = getSongs(url)
    except:
        return jsonify({"functionSuccess": 0, "errorMessage": "Error getting songs"})

    if fnSuccess == False:
        return jsonify({"functionSuccess": 0, "errorMessage": "given playlist could not be reached"})

    if not name:
        name = giveRandomName()

    try:    
        missingSongs = YTMusicAPI.makeYTPlaylist(songs_data, name)
        return jsonify({"functionSuccess": 1, "missingSongs": missingSongs, "name": name})
    except:
        return jsonify({"functionSuccess": 0, "errorMessage": "Error creating playlist"})

# TESTING  -- TODO REMOVE LATER
@app.route('/api/false', methods=['POST'])
def testFalse():    
    return jsonify({"functionSuccess": 0, "errorMessage": "lalala error"})


@app.route('/api/true', methods=['POST'])
def testTrue():
    return jsonify({"functionSuccess": 1, "errorMessage": "lalala no error", "name": "cheeseBorger"})



app.run(host="127.0.0.1", port="5000")