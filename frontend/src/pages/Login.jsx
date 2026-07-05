import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = async (e) => {
    e.preventDefault();

    try {
      const formData = new URLSearchParams();
      formData.append("username", email);
      formData.append("password", password);

      const res = await api.post("/auth/login", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      localStorage.setItem("token", res.data.access_token);
      localStorage.setItem("user_email", email);

      navigate("/dashboard");
    } catch (err) {
      alert("Invalid Email or Password");
      console.error(err);
    }
  };

  return (
    <div className="login-container">
      <form className="login-card glass-panel" onSubmit={login}>
        <h2><span><i className="bi bi-rocket-takeoff"></i> Distributed</span> Job Scheduler</h2>

        <input
          className="premium-input"
          type="email"
          placeholder="Email Address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          className="premium-input"
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit" className="premium-btn">
          Sign In <i className="bi bi-arrow-right-short"></i>
        </button>
      </form>
    </div>
  );
}

export default Login;