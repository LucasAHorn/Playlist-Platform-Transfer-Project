import { useState } from "react";
import "./app.css";

function App() {
  const [playlistUrl, setPlaylistUrl] = useState<string>("");
  const [name, setName] = useState<string>("");

  async function serverInteractionHandling(APIEndpoint: string) {

    if (playlistUrl.length == 0) {
      alert("Enter a playlist URL for any supported platform");
      return;
    }

    const bodyData = JSON.stringify({ url: playlistUrl, name });

    try {
      const response = await fetch(APIEndpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: bodyData,
      });

      if (!response.ok) {
        console.log(response);
        alert("Failed to communicate with the server");
      }

      const data = await response.json();

      if (data.functionSuccess === 1) {
        alert("Successfully Created Playlist!");
      } else {
        alert("Failed Creating Playlist\n" + data.errorMessage);
      }
    } catch (error) {
      console.log(error);
      alert("Error occurred while processing the request.");
    }
  }

  async function ToSpotify() {
    serverInteractionHandling("/api/ToSpotify");
  }

  async function Testing(success: boolean) {
    console.log("/Testing/" + success);
    serverInteractionHandling("/api/" + success);
  }

  return (
    <div className="LandingArea">
      <h1>Playlist Transfer Project</h1>
      <p>This website will transfer a YouTube Music playlist to Spotify</p>
      <h2>Functional: smaller playlists</h2>
      <div>
        <form className="VerticallyAligned" onSubmit={ToSpotify}>
          <div className="HorizontallyAligned">
            <input
              className="AnswerOptions"
              type="text"
              placeholder="Enter Playlist Link"
              onChange={(event) => setPlaylistUrl(event.target.value)}
            />
          </div>

          <div className="HorizontallyAligned">
            <input
              className="AnswerOptions"
              type="text"
              placeholder="Enter New Playlist Name"
              onChange={(event) => setName(event.target.value)}
            />
          </div>
          <div className="HorizontallyAligned">
            <button className="AnswerOptions" type="submit" onClick={() => ToSpotify()}>
              TRANSFER
            </button>
          </div>
        </form>
        <div className="HorizontallyAligned">
          <button className="AnswerOptions" type="button" onClick={() => Testing(true)}>
            Test Success
          </button>
          <button className="AnswerOptions" type="button" onClick={() => Testing(false)}>
            Test Failure
          </button>
        </div>
      </div>
      </div>
  );
}

export default App;
