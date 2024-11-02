from flask import jsonify
from ytmusicapi import YTMusic
import Creds


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

    songCounter = 0 # TODO: delete after testing
    songs_data = []

    if "tracks" in dictOfPlaylist:
        for track in dictOfPlaylist["tracks"]:
            songCounter += 1 # TODO: delete after testing
            
            title = cleanTitle(track["title"])
            artists = [artist["name"] for artist in track["artists"]]

            songs_data.append({
                "title": title,
                "artists": artists
            })
    
    print(songCounter) # TODO: delete after done testing
    return songs_data


def makeYTPlaylist(songs_data, playlistName):

    projectNumber, Project_ID = Creds.getYTMusicCreds()

    # get auth 
    
    # make new playlist

    # add songs to playlist

    missingSongs = [] # contains a song and artists

    return missingSongs


# Main run here for testing purposes
# getYTSongs("https://music.youtube.com/playlist?list=RDCLAK5uy_nmS3YoxSwVVQk9lEQJ0UX4ZCjXsW_psU8")
# 
# potential url: https://music.youtube.com/playlist?list=RDCLAK5uy_m0U8h6HP_YFe0riaCUUWx9fMXCVPGxlso&playnext=1&feature=shared