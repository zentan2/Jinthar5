import React from "react";

import './bstest.css';
import { useNavigate } from 'react-router-dom';

const BSTest = () => {
  const navigate = useNavigate();

  function handleSubmit(e) {
    e.preventDefault();
    console.log(e.target.email.value);

    if (!e.target.email.value) {
      alert("You have succesfully added QTY of Ticker @ Price");
    } 
    else if (!e.target.email.value) {
      alert("Valid email is required");
    } 
    else if (!e.target.password.value) {
      alert("Password is required");
    } 
    else if (
      e.target.email.value === "me@example.com" &&
      e.target.password.value === "123456"
    ) {
      alert("Successfully logged in");
           
    } 
    else {
      alert("Wrong email or password combination");
    }
  };

  function handleClick (e){
    e.preventDefault();
    alert("You have succesfully removed QTY of Ticker @ Price");
  };

  function handleSearch(e){
    e.preventDefault();
    alert("Searching Ticker / Company Name");
  };


    return (
      <div className="Login">
         <form className="form" onSubmit={handleSubmit}>
         <div className="input-group">
            <label htmlFor="ticker">Ticker </label>
            <input type="ticker" name="ticker" />
          </div>
          <button className="secondary" onClick={handleSearch}>
          Search
        </button>
          <div className="input-group">
            <label htmlFor="email">Quantity </label>
            <input type="email" name="email" />
          </div>
          <div className="input-group">
            <label htmlFor="password">Cost </label>
            <input type="password" name="password" />
          </div>
          <button className="primary">Update - Add</button>
        </form>
        <button className="secondary" onClick={handleClick}>
          Update - Minus
        </button>
      </div>
    );
  
}

export default BSTest;