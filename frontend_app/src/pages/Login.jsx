import React, { useState } from "react";
import { loginUser, registerUser } from "../services/userService";

export default function Login({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isRegister, setIsRegister] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      if (isRegister) {
        await registerUser({ email, password });
        setIsRegister(false);
        setError("Registration successful. Please login.");
      } else {
        const res = await loginUser({ email, password });
        onLogin(email); // You may want to store token: res.access_token
      }
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div style={{ maxWidth: 300, margin: "auto", padding: 20 }}>
      <h2>{isRegister ? "Register" : "Login"}</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={{ width: "100%", marginBottom: 10 }}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{ width: "100%", marginBottom: 10 }}
        />
        <button type="submit" style={{ width: "100%" }}>
          {isRegister ? "Register" : "Login"}
        </button>
      </form>
      <button
        onClick={() => {
          setIsRegister((v) => !v);
          setError("");
        }}
        style={{ width: "100%", marginTop: 10 }}
      >
        {isRegister ? "Go to Login" : "Create Account"}
      </button>
      {error && <div style={{ color: "red", marginTop: 10 }}>{error}</div>}
    </div>
  );
}
