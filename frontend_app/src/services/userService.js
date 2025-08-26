import { saveToken, getToken, getAuthHeaders } from "./utility";
import { BASE_URL } from "./constants";

export async function authFetch(url, options = {}) {
  const headers = {
    ...(options.headers || {}),
    ...getAuthHeaders(),
    "Content-Type": "application/json",
  };
  const res = await fetch(url, { ...options, headers });
  if (!res.ok) throw new Error("API request failed");
  return res.json();
}

export async function registerUser({ email, password }) {
  const res = await fetch(`${BASE_URL}/user/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) throw new Error("Registration failed");
  return res.json();
}

export async function loginUser({ email, password }) {
  const res = await fetch(`${BASE_URL}/user/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) throw new Error("Login failed");
  const data = await res.json();
  if (data.access_token) saveToken(data.access_token);
  return data;
}
