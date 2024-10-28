import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/form.css";

function Form({ route, method }) {
  const [mail, setUserMail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const formName = method === "login" ? "Login" : "Register";

  const handleSubmit = async (e) => {
    setLoading(true);
    // prevent default behavior of reloading the page on submit
    e.preventDefault();

    try {
      const res = await api.post(route, { mail, password });
      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
        navigate("/");
      } else {
        navigate("/login");
      }
    } catch (error) {
      alert(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <h1>{formName}</h1>
      <input
        className="form-input"
        type="text"
        value={mail}
        onChange={(e) => setUserMail(e.target.value)}
        placeholder="Mail"
      />
      <input
        className="form-input"
        type="text"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button className="form-button" type="submit">
        Submit
      </button>
    </form>
  );
}

export default Form;
