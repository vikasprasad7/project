import React, { useState } from "react";
import axios from "axios";

export default function ChatBox() {
  const [message, setMessage] = useState("");
  const [formData, setFormData] = useState(null);

  const sendMessage = async () => {
    const res = await axios.post("http://localhost:5000/chat", {
      user_name: "Vikas",  // dynamic in real app
      message
    });
    setFormData(res.data);
  };

  return (
    <div>
      <h2>Healthcare Communication Chat</h2>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter details of your communication..."
      />
      <button onClick={sendMessage}>Send</button>

      {formData && (
        <div>
          <h3>Extracted Form</h3>
          <form>
            <label>Professional Name</label>
            <input type="text" value={formData.professional_name} readOnly />

            <label>Date</label>
            <input type="text" value={formData.date} readOnly />

            <label>Time</label>
            <input type="text" value={formData.time} readOnly />

            <label>Sentiment</label>
            <input type="text" value={formData.sentiment} readOnly />
          </form>
        </div>
      )}
    </div>
  );
}
