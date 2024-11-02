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
    if(url.index("spotify.com") != -1):
        return True, SpotifyAPI.getSpotifySongs(url)

    if(url.index("music.youtube.com")):
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


    if not fnSuccess:
        return jsonify({"functionSuccess": 0, "errorMessage": "given playlist could not be reached"})
    
    if not name:
        name = giveRandomName()
    
    try:
        return SpotifyAPI.createPlaylist(song_data, name)
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

    if not fnSuccess:
        return jsonify({"functionSuccess": 0, "errorMessage": "given playlist could not be reached"})

    if not name:
        name = giveRandomName()

    try:    
        return YTMusicAPI.makeYTPlaylist(songs_data, name)
    except:
        return jsonify({"functionSuccess": 0, "errorMessage": "Error creating playlist"})

# TESTING  -- TODO REMOVE LATER
@app.route('/Testing/false')
def testFalse():
    return jsonify({"functionSuccess": 1, missingSongs:"lalala - use proper formatting"})

@app.route('/Testing/true')
def testTrue():
    return jsonify({"functionSuccess": 1, "errorMessage": "lalala error"})



app.run(host="127.0.0.1", port="5000")