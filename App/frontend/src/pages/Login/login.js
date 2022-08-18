import React from "react";
import logo from "../../assets/citi.png";
import "./login.css";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();
  document.title = "Login";
  function handleSubmit(e) {
    e.preventDefault();
    console.log(e.target.email.value);

    if (!e.target.email.value) {
      alert("Email is required");
    } else if (!e.target.email.value) {
      alert("Valid email is required");
    } else if (!e.target.password.value) {
      alert("Password is required");
    } else if (
      e.target.email.value === "me@example.com" &&
      e.target.password.value === "123456"
    ) {
      alert("Successfully logged in");
      navigate("/portfolio");
    } else {
      alert("Wrong email or password combination");
    }
  }

  function handleClick(e) {
    e.preventDefault();
    navigate("/signup");
  }

  return (
    <div className="Login">
      <img src={logo} className="logo" alt="citi-logo" />
      <form className="form" onSubmit={handleSubmit}>
        <div className="input-group">
          <label htmlFor="email">Email </label>
          <input type="email" name="email" />
        </div>
        <div className="input-group">
          <label htmlFor="password">Password </label>
          <input type="password" name="password" />
        </div>
        <button className="primary">Log In</button>
      </form>
      <button className="secondary" onClick={handleClick}>
        Sign Up
      </button>
    </div>
  );
};

export default Login;
