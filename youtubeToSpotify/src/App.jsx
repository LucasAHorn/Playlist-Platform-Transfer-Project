import { useState } from "react";
import "./App.css";

/**
 * This page is a landing area for users and can be
 * @author LucasAHorn
 */
function App() {
  const [playlistUrl, setPlaylistUrl] = useState("");

  /**
   * This function will redirect the user to the spotify login
   * Then create the new playlist if token is valid **use rand to make the playlist name different every time**
   * Then hopefully scrape the artist name and song name and find the closest match
   *
   */
  function YoutubeToSpotify() {}

  /**
   * This will be implimented later
   * This will be the
   */
  function SpotifyToYoutube() {
    console.log(playlistUrl);
  }

  return (
    <>
      <div className="LandingArea">
        <h1>Playlist Transfer Project</h1>
        <p>This website can transfer a public playlist to another platform</p>
        <p>currently functional: NONE</p>
        <div>
          <form>
            <p>
              Public playlist url:
              <input
                type="text"
                id="playlistUrl"
                name="playlistUrl"
                placeholder="Enter a playlist link..."
                onChange={(event) => setPlaylistUrl(event.target.value)}
              ></input>
            </p>
            <button type="submit" onClick={YoutubeToSpotify()}>
              Youtube to Spotify
            </button>
            <button type="submit" onClick={SpotifyToYoutube()}>
              Spotify to Youtube
            </button>
          </form>
        </div>
      </div>
      <div display="none"></div>
    </>
  );
}
export default App;
