import React, { useState } from "react";
import Login from "./pages/Login";
import Projects from "./pages/Projects";
import Tasks from "./pages/Tasks";

function App() {
  const [user, setUser] = useState(null);
  const [selectedProject, setSelectedProject] = useState(null);

  if (!user) {
    return <Login onLogin={setUser} />;
  }

  return (
    <div style={{ padding: 20 }}>
      <div style={{ marginBottom: 20 }}>
        <span>Welcome, {user}! </span>
        <button
          onClick={() => {
            setUser(null);
            setSelectedProject(null);
          }}
        >
          Logout
        </button>
      </div>
      <Projects onSelect={setSelectedProject} />
      <Tasks project={selectedProject} />
    </div>
  );
}

export default App;
