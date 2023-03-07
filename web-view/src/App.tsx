import React, { useEffect, useState } from "react";
import "./App.css";

const _window = window as any;

function App() {
  const [hasPywebview, setHasPywebview] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    onInit();
  }, []);

  const onInit = () => {
    if (_window?.pywebview) {
      setHasPywebview(true);

      // Expose setMessage in order to call it from Python
      _window.pywebview.state = {};
      _window.pywebview.state.setMessage = setMessage;
    }
  };

  const sendMessage = () => {
    const time = new Date().getTime();
    _window.pywebview.api.send_message(`PING (${time})`);
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>Hooked up with Phyton app: {hasPywebview ? "Yes" : "No"}</p>

        <p>Message revieved: {message.length ? message : "-"}</p>

        <button onClick={sendMessage}>PING</button>
      </header>
    </div>
  );
}

export default App;
