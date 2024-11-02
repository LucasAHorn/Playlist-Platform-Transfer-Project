import React, { useState } from "react";
import "./app.css";
import Message from "./Message"; // Import Message component

function App() {
  const [playlistUrl, setPlaylistUrl] = useState("");
  const [name, setName] = useState("");
  const [message, setMessage] = useState<string | null>(null);
  const [isSuccess, setIsSuccess] = useState(false);

  async function serverInteractionHandling(APIEndpoint: string) {
    const bodyData = JSON.stringify({ url: playlistUrl, name: name });

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
        setMessage("Operation was successful!");
        setIsSuccess(true);
      } else {
        setMessage("Data was wrong");
        setIsSuccess(false);
      }
    } catch (error) {
      console.log(error)
    }
  }


  // TODO: implement a way to make the button have a 5 sec delay between uses
  async function ToSpotify() {
    serverInteractionHandling('/api/ToSpotify');
  }

  async function ToYoutube() {
    serverInteractionHandling('/api/ToYTMusic');
  }

  async function Testing(success:boolean) {
    console.log('/Testing/' + success);
    serverInteractionHandling('/Testing/' + success);
  }

  return (
    <div className="LandingArea">
      <h1>Playlist Transfer Project</h1>
      <p>This website will transfer a public playlist to another platform</p>
      <p>currently functional: NONE</p>
      <div>
        <form className="VerticallyAligned" onSubmit={(event) => event.preventDefault()}>
          <div className="HorizontallyAligned">
            <p className="AnswerOptions">Public playlist url:</p>
            <input
              className="AnswerOptions"
              type="text"
              placeholder="Enter playlist link"
              onChange={(event) => setPlaylistUrl(event.target.value)}
            />
          </div>

          <div className="HorizontallyAligned">
            <p className="AnswerOptions">Optional new playlist name:</p>
            <input
              className="AnswerOptions"
              type="text"
              placeholder="Enter new playlist name"
              onChange={(event) => setName(event.target.value)}
            />
          </div>

          <div className="HorizontallyAligned">
            <button className="AnswerOptions" type="button" onClick={() => ToSpotify()}>
              To Spotify
            </button>
            <button className="AnswerOptions" type="button" onClick={() => ToYoutube()}>
              To Youtube Music
            </button>
          </div>

          <div className="HorizontallyAligned">
            <button className="AnswerOptions" type="button" onClick={() => Testing(true)}>
              Test Success
            </button>
            <button className="AnswerOptions" type="button" onClick={() => Testing(false)}>
              Test Failure
            </button>
          </div>

        </form>

        {/* Display message if available */}
        {message && <Message text={message} success={isSuccess} />}
      </div>
    </div>
  );
}

export default App;
