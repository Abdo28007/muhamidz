// AvocatSignUp.js
import React, { useState } from "react";
import { Link } from 'react-router-dom';
import './AvocatSignUp.css'

import LoginPage from './LoginPage';
const AvocatSignUp = () => {
  const [avocatData, setAvocatData] = useState({
    name: "",
    email: "",
    specialization: "",
    address: "",
    phone: "",
    password: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setAvocatData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("your_avocat_signup_api_url", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(avocatData),
      });

      if (response.ok) {
        // Avocat signup successful
        console.log("Avocat Signup Successful");
      } else {
        // Handle error
        console.error("Avocat Signup Failed");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };
  const handleLoginClick = () => {
    // Navigate to the login page
    // You can implement this navigation based on your routing system (e.g., React Router)
    console.log('Navigate to login page');
  };

  return (
   
    <div>
        <h2>Sign Up</h2>

    <form onSubmit={handleSubmit}>
    <label>
      Name:
      <input
        type="text"
        name="name"
        value={avocatData.name}
        onChange={handleChange}
      />
    </label>
    <label>
      Email:
      <input
        type="email"
        name="email"
        value={avocatData.email}
        onChange={handleChange}
      />
    </label>
    <label>
      Specialization:
      <input
        type="text"
        name="specialization"
        value={avocatData.specialization}
        onChange={handleChange}
      />
    </label>
    <label>
      Address:
      <input
        type="text"
        name="address"
        value={avocatData.address}
        onChange={handleChange}
      />
    </label>
    <label>
      Phone:
      <input
        type="tel"
        name="phone"
        value={avocatData.phone}
        onChange={handleChange}
      />
    </label>
    <label>
      Password:
      <input
        type="password"
        name="password"
        value={avocatData.password}
        onChange={handleChange}
      />
    </label>
    <button type="submit">Sign Up</button>
  </form>
  <Link to='/LoginPage'><button onClick={handleLoginClick}>Login</button></Link>
  </div>
   
  );
};

export default AvocatSignUp;
