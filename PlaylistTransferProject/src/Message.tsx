import React from "react";
import "./Message.css";

interface MessageProps {
  text: string | null;
  playlistName: string | null;
  success: boolean;
  onDismiss: () => void;
}

const Message: React.FC<MessageProps> = ({ text, playlistName, success, onDismiss }) => {
  return success ? (
    <div className="MessageSuccess">
      <p>Successfully created playlist: {playlistName}</p>
      <button className="dismiss-button" onClick={onDismiss}>
        &times;
      </button>
    </div>
  ) : (
    <div className="MessageError">
      <p>{text}</p>
      <button className="dismiss-button" onClick={onDismiss}>
        &times;
      </button>
    </div>
  );
};

export default Message;
