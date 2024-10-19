import { useState } from "react";
import "./app.css";

function App() {
  const [playlistUrl, setPlaylistUrl] = useState("");
  const [token, setToken] = useState("");

  /**
   * Async function to handle YouTube to Spotify transfer.
   */
  async function YoutubeToSpotify() {

    // This tests is the input to url is "Lucas" and then prints it to terminal after a flask server checks for validity
    try {
      const response = await fetch('/api/YoutubeToSpotify', {  // Use correct API endpoint
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: playlistUrl }),  // Send the name to the backend
      });

      if (!response.ok) {
        throw new Error('Request failed');
      }

      const data = await response.json();

      // Check response data and log accordingly
      if (data.functionSuccess === 1) {
        console.log("Data successfully sent and received");
      } else {
        console.log("Data was wrong");
      }

    } catch (error) {
      console.log('Error:', error);
    }
  }


  /**
   * This will be implimented later
  */
 function SpotifyToYoutube() {
   console.log("Spotify to Youtube");
   console.log(playlistUrl);
   console.log(token);
   // window.open("https://" + newPlaylistUrl, "_blank")?.focus(); // TODO: use this to open the playlist after it is made
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