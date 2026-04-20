import React, { useState } from "react";
import "./App.css";

function App() {
  const [user, setUser] = useState(null);

  const skills = [
    "Web Development",
    "Graphic Design",
    "Video Editing",
    "Public Speaking"
  ];

  return (
    <div className="App">
      <h1>SkillSwap Community</h1>

      {!user ? (
        <button onClick={() => setUser("User")}>Login</button>
      ) : (
        <div>
          <h2>Welcome, {user}</h2>
          <h3>Available Skills</h3>
          <ul>
            {skills.map((skill, index) => (
              <li key={index}>
                {skill}
                <button style={{ marginLeft: "10px" }}>
                  Request
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;