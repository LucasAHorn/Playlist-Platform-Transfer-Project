from ytmusicapi import YTMusic


def getSongs(playlistUrl):
    ytmusic = YTMusic()

    # This can be any playlist url
    # playlistUrl = "https://music.youtube.com/playlist?list=RDCLAK5uy_lJ8xZWiZj2GCw7MArjakb6b0zfvqwldps"

    playlist_id = playlistUrl.split("list=")[1]

    dictOfPlaylist = ytmusic.get_playlist(playlist_id)

    songCounter = 0

    if "tracks" in dictOfPlaylist:
        for track in dictOfPlaylist["tracks"]:
            # if (songCounter >= 10):
            #     break
            songCounter += 1
            # Get the song title
            title = track["title"]
            # Get the artists and join them into a single string
            artists = ', '.join([artist["name"] for artist in track["artists"]])
            # Print the song title with the artists
            print(f"{songCounter}. {title} by {artists}")

    print(f"\t{songCounter} songs total")

# Main run here
# getSongs("https://music.youtube.com/playlist?list=RDCLAK5uy_kaYR5k7pkTcxU8A6Tgz0Z4ikrAF2uTIiU")