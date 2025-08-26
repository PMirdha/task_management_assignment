import React, { useState, useEffect } from "react";
import {
  fetchProjects,
  createProject,
  deleteProject,
} from "../services/projectService";

export default function Projects({ onSelect }) {
  const [projects, setProjects] = useState([]);
  const [showAdd, setShowAdd] = useState(false);
  const [newName, setNewName] = useState("");
  const [newDesc, setNewDesc] = useState("");
  const [dropdownOpen, setDropdownOpen] = useState(null); // project id for open dropdown

  useEffect(() => {
    fetchProjects()
      .then((data) => setProjects(data))
      .catch(() => setProjects([]));
  }, []);

  const handleAddProject = async (e) => {
    e.preventDefault();
    if (newName.trim()) {
      try {
        const created = await createProject({
          name: newName,
          description: newDesc,
        });
        setProjects((prev) => [...prev, created]);
      } catch {}
      setNewName("");
      setNewDesc("");
      setShowAdd(false);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteProject(id);
      setProjects((prev) => prev.filter((p) => p.id !== id));
    } catch (err) {
      if (err instanceof Error) {
        alert(err.message); // Show error detail in toast
      }
    }
    setDropdownOpen(null);
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20 }}>
      <h2>Projects</h2>
      <button onClick={() => setShowAdd(!showAdd)} style={{ marginBottom: 16 }}>
        Add Project
      </button>
      {showAdd && (
        <form onSubmit={handleAddProject} style={{ marginBottom: 16 }}>
          <input
            type="text"
            placeholder="Project Name"
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
            required
            style={{ marginRight: 8 }}
          />
          <input
            type="text"
            placeholder="Description"
            value={newDesc}
            onChange={(e) => setNewDesc(e.target.value)}
            style={{ marginRight: 8 }}
          />
          <button type="submit">Save</button>
        </form>
      )}
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th
              style={{
                borderBottom: "1px solid #ccc",
                textAlign: "left",
                padding: "8px",
              }}
            >
              Name
            </th>
            <th
              style={{
                borderBottom: "1px solid #ccc",
                textAlign: "left",
                padding: "8px",
              }}
            >
              Description
            </th>
            <th
              style={{
                borderBottom: "1px solid #ccc",
                textAlign: "center",
                padding: "8px",
              }}
            >
              Actions
            </th>
          </tr>
        </thead>
        <tbody>
          {projects.map((project) => (
            <tr key={project.id}>
              <td style={{ padding: "8px" }}>{project.name}</td>
              <td style={{ padding: "8px" }}>{project.description}</td>
              <td
                style={{
                  padding: "8px",
                  textAlign: "center",
                  position: "relative",
                }}
              >
                <button
                  onClick={() =>
                    setDropdownOpen(
                      dropdownOpen === project.id ? null : project.id
                    )
                  }
                  title="Actions"
                  style={{
                    background: "none",
                    border: "none",
                    fontSize: "24px",
                    cursor: "pointer",
                  }}
                >
                  &#8942; {/* horizontal 3 dots */}
                </button>
                {dropdownOpen === project.id && (
                  <div
                    style={{
                      position: "absolute",
                      top: "36px",
                      right: "0",
                      background: "#fff",
                      border: "1px solid #ccc",
                      boxShadow: "0 2px 8px rgba(0,0,0,0.15)",
                      zIndex: 10,
                      minWidth: "120px",
                    }}
                  >
                    <button
                      onClick={() => {
                        onSelect(project);
                        setDropdownOpen(null);
                      }}
                      style={{
                        display: "block",
                        width: "100%",
                        padding: "8px",
                        border: "none",
                        background: "none",
                        textAlign: "left",
                        cursor: "pointer",
                      }}
                    >
                      View Tasks
                    </button>
                    <button
                      onClick={() => handleDelete(project.id)}
                      style={{
                        display: "block",
                        width: "100%",
                        padding: "8px",
                        border: "none",
                        background: "none",
                        textAlign: "left",
                        color: "red",
                        cursor: "pointer",
                      }}
                    >
                      Delete
                    </button>
                  </div>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
