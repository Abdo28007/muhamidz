// LoginPage.js
import React from "react";
import { Link } from "react-router-dom";
import "./LoginPage.css";
const LoginPage = () => {
  // Add logic for handling login and navigation

  const handleAccusedSignUp = () => {
    // Navigate to the accused signup page
    // You can implement this navigation based on your routing system (e.g., React Router)
    console.log("Navigate to accused signup page");
  };

  const handleAvocatSignUp = () => {
    // Navigate to the avocat signup page
    // You can implement this navigation based on your routing system (e.g., React Router)
    console.log("Navigate to avocat signup page");
  };

  return (
    <div>
      <h2>Login</h2>
      <form>
        <label>
          Email:
          <input type="email" name="email" />
        </label>
        <label>
          Password:
          <input type="password" name="password" />
        </label>
       <Link to='/'> <button type="submit">Login</button></Link>
      </form>

      <div>
        <p>Don't have an account?</p>
        <Link to="/AccusedSignUp">
          <button onClick={handleAccusedSignUp}>Sign Up as Accused</button>
        </Link>
        <Link to="/AvocatSignUp">
          <button onClick={handleAvocatSignUp}>Sign Up as Avocat</button>
        </Link>
      </div>
    </div>
  );
};

export default LoginPage;
