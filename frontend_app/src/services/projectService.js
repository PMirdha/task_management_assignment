const BASE_URL = "http://localhost:8000"; // Change to your backend URL

export async function fetchProjects() {
  const res = await fetch(`${BASE_URL}/project/`);
  if (!res.ok) throw new Error("Failed to fetch projects");
  return res.json();
}

export async function createProject({ name, description }) {
  const res = await fetch(`${BASE_URL}/project/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, description }),
  });
  if (!res.ok) throw new Error("Failed to create project");
  return res.json();
}

export async function deleteProject(projectId) {
  const res = await fetch(`${BASE_URL}/project/${projectId}`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error("Failed to delete project");
  return res.json();
}
