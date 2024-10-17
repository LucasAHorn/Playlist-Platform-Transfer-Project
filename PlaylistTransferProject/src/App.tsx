import { useState } from "react";
import "./app.css";

function App() {
  const [playlistUrl, setPlaylistUrl] = useState("");
  const [token, setToken] = useState("");

  /**
   * This function will redirect the user to the spotify login
   * Then create the new playlist if token is valid **use rand to make the playlist name different every time**
   * Then hopefully scrape the artist name and song name and find the closest match
   *
   */
  function YoutubeToSpotify() {
    console.log("YouTube to spotify");
    console.log(playlistUrl);
    console.log(token);
    // window.open("https://" + newPlaylistUrl, "_blank")?.focus(); // TODO: use this to open the playlist after it is made
  }

  /**
   * This will be implimented later
   */
  function SpotifyToYoutube() {
    console.log("Spotify to Youtube");
    console.log(playlistUrl);
    console.log(token);
  }

  return (
    <div className="LandingArea">
      <h1>Playlist Transfer Project</h1>
      <p>This website will transfer a public playlist to another platform</p>
      <p>currently functional: NONE</p>
      <div>
        <form className="VerticallyAligned" onSubmit={(event) => event.preventDefault()}>
          
          <div className="HorizontallyAligned">
            <p className="AnswerOptions" >Public playlist url: </p>
            <input
              className="AnswerOptions" 
              type="text"
              name="playlistUrl"
              placeholder="Enter a playlist link..."
              onChange={(event) => setPlaylistUrl(event.target.value)}
            ></input>
          </div>
          
          <div className="HorizontallyAligned">
            <p className="AnswerOptions">Target Account Token: </p>
            <input
              className="AnswerOptions" 
              type="text"
              name="playlistUrl"
              placeholder="Enter the target acct token"
              onChange={(event) => setToken(event.target.value)}
            ></input>
          </div>

          <div className="HorizontallyAligned">
            <button className="AnswerOptions" type="button" onClick={() => YoutubeToSpotify()}>
              Youtube to Spotify
            </button>
            <button className="AnswerOptions" type="button" onClick={() => SpotifyToYoutube()}>
              Spotify to Youtube
            </button>
          </div>
        
        </form>
      </div>
    </div>
  );
}
export default App;