import { useState } from "react";
import "./app.css";

function App() {
  const [playlistUrl, setPlaylistUrl] = useState("");
  const [token, setToken] = useState("");
  const [name, setName] = useState("");


  /**
   * 
   * @param APIEndpoint 
   * @param bodyData 
   */
  async function serverInteractionHandling(APIEndpoint: string) {

    const bodyData = JSON.stringify({ url: playlistUrl, name: name, token: token });

    console.log(bodyData);

    try {
      const response = await fetch(APIEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: bodyData,
      });

      if (!response.ok) {
        throw new Error('Request failed');
      }

      const data = await response.json();

      if (data.functionSuccess === 1) {
        console.log(data);
      } else {
        console.log("Data was wrong");
      }

    } catch (error) {
      console.log('Error:', error);
    }
  }


  /**
   * Async function to handle YouTube to Spotify transfer.
   */
  async function YoutubeToSpotify() {
    // give more data in the json object
    serverInteractionHandling('/api/YTMusicToSpotify')
  }


  /**
   * This will be implimented later
  */
 function SpotifyToYoutube() {
    // give more data in the json object
    serverInteractionHandling('/api/SpotifyToYTMusic')
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
              placeholder="Enter playlist link"
              onChange={(event) => setPlaylistUrl(event.target.value)}
            ></input>
          </div>

          <div className="HorizontallyAligned">
            <p className="AnswerOptions">Target Account Token: </p>
            <input
              className="AnswerOptions" 
              type="text"
              placeholder="Enter the target acct token"
              onChange={(event) => setToken(event.target.value)}
            ></input>
          </div>

          <div className="HorizontallyAligned">
            <p className="AnswerOptions">Optional new name: </p>
            <input
              className="AnswerOptions" 
              type="text"
              placeholder="Enter new playlist name"
              onChange={(event) => setName(event.target.value)}
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