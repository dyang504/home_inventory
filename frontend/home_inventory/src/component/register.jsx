import React from "react";

function Register() {
  return (
    <div>
      <h2>Home Inventory Register</h2>
      <form>
        <label>
          username
          <input type="text" name="username" />
        </label>
        <label>
          passowrd
          <input type="text" name="password" />
        </label>
        <input type="submit" value="Register" />
      </form>
    </div>
  );
}

export default Register;
