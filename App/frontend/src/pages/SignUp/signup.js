import React from "react";
import logo from "../../assets/citi.png";
import "./signup.css";
import { useNavigate } from "react-router-dom";

const SignUp = () => {
  const navigate = useNavigate();
  document.title = "Sign Up";
  function handleSubmit(e) {
    e.preventDefault();
    console.log(e.target.email.value);

    if (!e.target.name.value) {
      alert("Name is required");
    } else if (!e.target.email.value) {
      alert("Email is required");
    } else if (!e.target.email.value) {
      alert("Valid email is required");
    } else if (!e.target.password.value) {
      alert("Password is required");
    } else if (!e.target.cpassword.value) {
      alert("Confirmed Password is required");
    } else if (e.target.password.value === e.target.cpassword.value) {
      alert("Signed Up Succesfull");
      navigate("/");
    } else {
      alert("Passwords do not match!");
    }
  }

  return (
    <div className="SignUp">
      <img src={logo} className="logo" alt="citi-logo" />
      <form className="form" onSubmit={handleSubmit}>
        <div className="input-group">
          <label htmlFor="name">Name </label>
          <input type="name" name="name" />
        </div>
        <div className="input-group">
          <label htmlFor="email">Email </label>
          <input type="email" name="email" />
        </div>
        <div className="input-group">
          <label htmlFor="password">Password </label>
          <input type="password" name="password" />
        </div>
        <div className="input-group">
          <label htmlFor="cpassword">Confirm Password </label>
          <input type="password" name="cpassword" />
        </div>
        <button className="primary">Sign Up</button>
      </form>
    </div>
  );
};

export default SignUp;
