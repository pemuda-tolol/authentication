import React from "react";
import {Link} from 'react-router-dom'

function PartForm() {
  // const linkStyle = {
  //   textDecoration: "none"
  // }

  return (
    <form>
      <label for="username">Username:</label>
      <input type="text" placeholder="Username" id="username" required/>
      <label for="password">Password:</label>
      <input type="password" placeholder="Password" id="password" required/>
      <div className="right">
        {/* <a href="#forgot-password" className="forgot-password">Forgot Password?</a> */}
        <Link to="/forgot-password" className="link">Forgot Password?</Link>
      </div>
      <input type="button" value="Log In" className="login-btn" />
      <div className="center">
        Do not have an account? {" "}
        <Link to="/signup" className="link">
            Create an account
        </Link>
      </div>
    </form>
  );
}

export default PartForm;
