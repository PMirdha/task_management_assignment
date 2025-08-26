import React, { useState, useEffect } from "react";
import {
  fetchTasks,
  createTask,
  updateTask,
  updateTaskStatus,
} from "../services/taskService";

const statusOptions = ["pending", "in-progress", "completed"];

export default function Tasks({ project }) {
  const [tasks, setTasks] = useState([]);
  const [dropdownOpen, setDropdownOpen] = useState(null);
  const [editTaskId, setEditTaskId] = useState(null);
  const [editDesc, setEditDesc] = useState("");
  const [editStatus, setEditStatus] = useState(statusOptions[0]);
  const [showAdd, setShowAdd] = useState(false);
  const [newDesc, setNewDesc] = useState("");
  const [newStatus, setNewStatus] = useState(statusOptions[0]);
  const [statusModal, setStatusModal] = useState({ open: false, taskId: null });
  const [modalStatus, setModalStatus] = useState(statusOptions[0]);

  useEffect(() => {
    if (project) {
      fetchTasks()
        .then((data) => {
          setTasks(data.filter((t) => t.project_id === project.id));
        })
        .catch(() => setTasks([]));
    }
  }, [project]);

  if (!project)
    return <div style={{ padding: 20 }}>Select a project to view tasks.</div>;

  const handleStatusChange = async (taskId, newStatus) => {
    try {
      const updated = await updateTaskStatus(taskId, newStatus);
      setTasks((prev) => prev.map((t) => (t.id === taskId ? updated : t)));
    } catch {}
    setStatusModal({ open: false, taskId: null });
  };

  const handleEdit = (taskId) => {
    const task = tasks.find((t) => t.id === taskId);
    setEditTaskId(taskId);
    setEditDesc(task.title);
    setEditStatus(task.status);
    setDropdownOpen(null);
  };

  const handleEditSave = async () => {
    try {
      const updated = await updateTask(editTaskId, {
        title: editDesc,
        status: editStatus,
      });
      setTasks((prev) => prev.map((t) => (t.id === editTaskId ? updated : t)));
    } catch {}
    setEditTaskId(null);
    setEditDesc("");
  };

  const handleAddTask = async (e) => {
    e.preventDefault();
    if (!newDesc.trim()) return;
    try {
      const created = await createTask({
        project_id: project.id,
        title: newDesc,
        status: newStatus,
      });
      setTasks((prev) => [...prev, created]);
    } catch (err) {
      if (err instanceof Error) {
        alert(err.message); // Show error detail in alert
      }
    }
    setNewDesc("");
    setNewStatus(statusOptions[0]);
    setShowAdd(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20 }}>
      <h2>Tasks for {project.name}</h2>
      <button onClick={() => setShowAdd(!showAdd)} style={{ marginBottom: 16 }}>
        Add Task
      </button>
      {showAdd && (
        <form onSubmit={handleAddTask} style={{ marginBottom: 16 }}>
          <input
            type="text"
            placeholder="Task Description"
            value={newDesc}
            onChange={(e) => setNewDesc(e.target.value)}
            required
            style={{ marginRight: 8 }}
          />
          <select
            value={newStatus}
            onChange={(e) => setNewStatus(e.target.value)}
            style={{ marginRight: 8 }}
          >
            {statusOptions.map((status) => (
              <option key={status} value={status}>
                {status.charAt(0).toUpperCase() + status.slice(1)}
              </option>
            ))}
          </select>
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
              Description
            </th>
            <th
              style={{
                borderBottom: "1px solid #ccc",
                textAlign: "center",
                padding: "8px",
              }}
            >
              Status
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
          {tasks.map((task) => (
            <tr key={task.id}>
              <td style={{ padding: "8px" }}>
                {editTaskId === task.id ? (
                  <>
                    <input
                      type="text"
                      value={editDesc}
                      onChange={(e) => setEditDesc(e.target.value)}
                      style={{ marginRight: 8 }}
                    />
                    <select
                      value={editStatus}
                      onChange={(e) => setEditStatus(e.target.value)}
                      style={{ marginRight: 8 }}
                    >
                      {statusOptions.map((status) => (
                        <option key={status} value={status}>
                          {status.charAt(0).toUpperCase() + status.slice(1)}
                        </option>
                      ))}
                    </select>
                    <button onClick={handleEditSave}>Save</button>
                    <button
                      onClick={() => setEditTaskId(null)}
                      style={{ marginLeft: 4 }}
                    >
                      Cancel
                    </button>
                  </>
                ) : (
                  task.title
                )}
              </td>
              <td style={{ padding: "8px", textAlign: "center" }}>
                {task.status}
              </td>
              <td
                style={{
                  padding: "8px",
                  textAlign: "center",
                  position: "relative",
                }}
              >
                <button
                  onClick={() =>
                    setDropdownOpen(dropdownOpen === task.id ? null : task.id)
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
                {dropdownOpen === task.id && (
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
                      onClick={() => handleEdit(task.id)}
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
                      Edit
                    </button>
                    <button
                      onClick={() => {
                        setStatusModal({ open: true, taskId: task.id });
                        setModalStatus(task.status);
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
                      Change Status
                    </button>
                  </div>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {/* Status Change Modal */}
      {statusModal.open && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100vw",
            height: "100vh",
            background: "rgba(0,0,0,0.2)",
            zIndex: 100,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <div
            style={{
              background: "#fff",
              padding: 24,
              borderRadius: 8,
              boxShadow: "0 2px 16px rgba(0,0,0,0.2)",
              minWidth: 300,
            }}
          >
            <h3>Change Task Status</h3>
            <select
              value={modalStatus}
              onChange={(e) => setModalStatus(e.target.value)}
              style={{ marginBottom: 16, width: "100%" }}
            >
              {statusOptions.map((status) => (
                <option key={status} value={status}>
                  {status.charAt(0).toUpperCase() + status.slice(1)}
                </option>
              ))}
            </select>
            <div style={{ textAlign: "right" }}>
              <button
                onClick={() => setStatusModal({ open: false, taskId: null })}
                style={{ marginRight: 8 }}
              >
                Cancel
              </button>
              <button
                onClick={() =>
                  handleStatusChange(statusModal.taskId, modalStatus)
                }
                style={{ background: "#007bff", color: "#fff" }}
              >
                Save
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
