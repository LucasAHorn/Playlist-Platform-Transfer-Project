from flask import jsonify
from ytmusicapi import YTMusic


# This cleans the YT title to make it more clear
def cleanTitle(title):
    #TODO: add code manipulation here
    return title


# This takes in a ytmusic playlist url and returns a json of song titles and song aritsts
def getYTSongs(playlistUrl):

    ytmusic = YTMusic()

    # Handle url issues
    playlist_id = playlistUrl.split("list=")[1].split("&playnext=")[0].split("&feature=")[0]
    dictOfPlaylist = ytmusic.get_playlist(playlist_id)

    songs_data = []

    if "tracks" in dictOfPlaylist:
        for track in dictOfPlaylist["tracks"]:
                               
            title = cleanTitle(track["title"])
            artists = [artist["name"] for artist in track["artists"]]

            songs_data.append({
                "title": title,
                "artists": artists
            })
    
    return songs_data


def makeYTPlaylist(songs_data, playlistName, token):
        
    missingSongs = []


    # testing return values
    missingSongs.append({
        "title": "Life is a Highway",
        "artists": ["Rascal Flatts"]
    })
    missingSongs.append({
        "title": "Shape of You",
        "artists": ["Ed Sheeran"]
    })

    return jsonify({"functionSuccess": 1, "missingSongs": missingSongs})


# Main run here for testing purposes
# print(getYTSongs("https://music.youtube.com/playlist?list=RDCLAK5uy_kaYR5k7pkTcxU8A6Tgz0Z4ikrAF2uTIiU"))
# 
# potential url: https://music.youtube.com/playlist?list=RDCLAK5uy_m0U8h6HP_YFe0riaCUUWx9fMXCVPGxlso&playnext=1&feature=shared