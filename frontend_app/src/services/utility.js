export function saveToken(token) {
    localStorage.setItem("access_token", token);
}

export function getToken() {
    return localStorage.getItem("access_token");
}

export function getAuthHeaders() {
    const token = getToken();
    return token ? { Authorization: `Bearer ${token}` } : {};
}
