import React, { useState } from 'react';
import './Message.css';

interface MessageProps {
  text: string;
  success: boolean;
}

const Message: React.FC<MessageProps> = ({ text, success }) => {
  const [visible, setVisible] = useState(true);

  const handleClose = () => {
    setVisible(false);
  };

  if (!visible) return null;

  return (
    <div className={`message ${success ? 'success' : 'error'}`}>
      <span>{text}</span>
      <button className="close-button" onClick={handleClose}>
        &times;
      </button>
    </div>
  );
};

export default Message;