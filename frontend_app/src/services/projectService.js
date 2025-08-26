import { getAuthHeaders } from "./utility";
import { BASE_URL } from "./constants";

export async function fetchProjects() {
  const res = await fetch(`${BASE_URL}/project/`, {
    headers: { ...getAuthHeaders() },
  });
  if (!res.ok) throw new Error("Failed to fetch projects");
  return res.json();
}

export async function createProject({ name, description }) {
  const res = await fetch(`${BASE_URL}/project/`, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...getAuthHeaders() },
    body: JSON.stringify({ name, description }),
  });
  if (!res.ok) throw new Error("Failed to create project");
  return res.json();
}

export async function deleteProject(projectId) {
  const res = await fetch(`${BASE_URL}/project/${projectId}`, {
    method: "DELETE",
    headers: { ...getAuthHeaders() },
  });
  if (!res.ok) {
    let detail = "Failed to delete project";
    try {
      const data = await res.json();
      if (data.detail) detail = data.detail;
    } catch { }
    throw new Error(detail);
  }
  return res.json();
}
