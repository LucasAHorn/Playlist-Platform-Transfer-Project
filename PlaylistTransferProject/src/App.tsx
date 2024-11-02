import { useState } from "react";
import "./app.css";
import Message from "./Message"; // Import Message component

interface Message {
  id: number;
  text: string | null;
  playlistName: string | null;
  success: boolean;
}

function App() {
  const [playlistUrl, setPlaylistUrl] = useState<string>("");
  const [name, setName] = useState<string>("");
  const [messages, setMessages] = useState<Message[]>([]);

  function addMessage(text: string | null, isSuccess: boolean, playlistName: string | null) {
    const newMessage: Message = {
      id: Date.now(),
      text,
      playlistName,
      success: isSuccess,
    };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
  }

  function dismissMessage(id: number) {
    setMessages((prevMessages) => prevMessages.filter((message) => message.id !== id));
  }

  async function serverInteractionHandling(APIEndpoint: string) {
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
        throw new Error("Request failed");
      }

      const data = await response.json();

      if (data.functionSuccess === 1) {
        addMessage(null, true, data.name);
      } else {
        addMessage(data.errorMessage, false, null);
      }
    } catch (error) {
      console.log(error);
      addMessage("An error occurred while processing the request.", false, null);
    }
  }

  async function ToSpotify() {
    serverInteractionHandling("/api/ToSpotify");
  }

  async function ToYoutube() {
    serverInteractionHandling("/api/ToYTMusic");
  }

  async function Testing(success: boolean) {
    console.log("/Testing/" + success);
    serverInteractionHandling("/api/" + success);
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

        {/* Display messages */}
        <div className="Messages">
          {messages.map((msg) => (
            <Message
              key={msg.id}
              text={msg.text}
              success={msg.success}
              playlistName={msg.playlistName}
              onDismiss={() => dismissMessage(msg.id)}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
