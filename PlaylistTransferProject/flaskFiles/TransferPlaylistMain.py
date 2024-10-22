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
        return data['url'], data['name'], data['token']


# Checks if there are obvious errors
def checkAPIForErrors(url, token, isSpotifyToken):
    if not (url):
        return jsonify({"functionSuccess": 0, "errorMessage": "url is invalid"})
    if not (token):     # TODO: make a better check here for if it is a valid token
        return jsonify({"functionSuccess": 0, "errorMessage": "token is invalid"})

    
# Gives an unnamed playlist a name
def giveRandomName():
    return f"RenameMe{random.randint(100000000, 1000000000)}"


# Transfers YT playlist to Spotify
@app.route('/api/YTMusicToSpotify', methods=['POST'])
def YTMusicToSpotify():
    url, name, token = getData()

    if checkAPIForErrors(url, token, 0):
        return checkAPIForErrors(url, token, 0)
    
    song_data = YTMusicAPI.getYTSongs(url)
    if not song_data:
        return jsonify({"functionSuccess": 0, "errorMessage": "given playlist could not be reached"})
    
    if not name:
        name = giveRandomName()
    # Should return a json of missing songs if it was successsful
    return SpotifyAPI.createPlaylist(song_data, name, token)


# Transfers a Spotify playlist to YT
@app.route('/api/SpotifyToYTMusic', methods=['POST'])
def SpotifyToYTMusic():
    url, name, token = getData()

    if checkAPIForErrors(url, token, 1):
        return checkAPIForErrors(url, token, 1)
    
    songs_data = SpotifyAPI.getSpotifySongs(url)
    if not songs_data:
        return jsonify({"functionSuccess": 0, "errorMessage": "given playlist could not be reached"})

    if not name:
        name = giveRandomName()
    return YTMusicAPI.makeYTPlaylist(songs_data, name, token)



app.run(host="127.0.0.1", port="5000")