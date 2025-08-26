const BASE_URL = "http://localhost:8000"; // Change to your backend URL

export async function fetchTasks() {
  const res = await fetch(`${BASE_URL}/task/`);
  if (!res.ok) throw new Error("Failed to fetch tasks");
  return res.json();
}

export async function fetchTask(taskId) {
  const res = await fetch(`${BASE_URL}/task/${taskId}`);
  if (!res.ok) throw new Error("Failed to fetch task");
  return res.json();
}

export async function createTask({ project_id, title, status }) {
  const res = await fetch(`${BASE_URL}/task/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ project_id, title, status }),
  });
  if (!res.ok) throw new Error("Failed to create task");
  return res.json();
}

export async function updateTask(taskId, { title, status }) {
  const res = await fetch(`${BASE_URL}/task/${taskId}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, status }),
  });
  if (!res.ok) throw new Error("Failed to update task");
  return res.json();
}

export async function updateTaskStatus(taskId, status) {
  const res = await fetch(`${BASE_URL}/task/${taskId}/status`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status }),
  });
  if (!res.ok) throw new Error("Failed to update task status");
  return res.json();
}

export async function deleteTask(taskId) {
  const res = await fetch(`${BASE_URL}/task/${taskId}`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error("Failed to delete task");
  return res.json();
}
