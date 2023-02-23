import React from 'react'
import {Link} from 'react-router-dom'

function PartFormSignUp() {
  return (
    <form>
        <label for="username">Username:</label>
        <input type="text" placeholder="Username" id="username" required/>
        <label for="password">Password:</label>
        <input type="password" placeholder="Password" id="password" required/>
        <label for="email">Email:</label>
        <input type="text" placeholder="Email" id="email" required/>
        <label for="name">Name:</label>
        <input type="text" placeholder="Name" id="name" required/>
        <label for="gender">Gender:</label><br/>
        <input type="radio" name="gender" id="male" value="male" />
        <label for="male">Male</label><br/>
        <input type="radio" name="gender" id="female" value="female" />
        <label for="female">Female</label><br/>
        <input type="button" value="Sign Up" className="sign-up-btn" />        
        <div className="center">
          Already a user? {" "}
          <Link to="/"  className="link">
              Log in
          </Link>
        </div>
    </form>
  )
}

export default PartFormSignUp