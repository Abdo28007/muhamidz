// AccusedSignUp.js
import React, { useState } from "react";
import "./AccusedSignUp.css";

import LoginPage from "./LoginPage";
import { Link } from "react-router-dom/cjs/react-router-dom.min";

const AccusedSignUp = () => {
  const [accusedData, setAccusedData] = useState({
    continent: "",
    name: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setAccusedData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add logic to handle accused signup data
    console.log("Accused Signup Data:", accusedData);
  };

  const handleLoginClick = () => {
    // Navigate to the login page
    // You can implement this navigation based on your routing system (e.g., React Router)

    console.log("Navigate to login page");
  };

  return (
    <div>
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit}>
        {/* <label>
        Continent:
        <input type="text" name="continent" value={accusedData.continent} onChange={handleChange} />
      </label> */}
        <label>
          Name:
          <input
            type="text"
            name="name"
            value={accusedData.name}
            onChange={handleChange}
          />
        </label>
        <label>
          Email:
          <input
            type="email"
            name="email"
            value={accusedData.email}
            onChange={handleChange}
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            name="password"
            value={accusedData.password}
            onChange={handleChange}
          />
        </label>
        <button type="submit">Sign Up</button>
      </form>
      <Link to='/LoginPage'>
      <button onClick={handleLoginClick}>
        Login
      </button></Link>
    </div>
  );
};

export default AccusedSignUp;
