import React from "react";

function Login() {
  return (
    <form>
      <h2>Home Inventory Login</h2>
      <label>
        username
        <input type="text" name="username" />
      </label>
      <label>
        passowrd
        <input type="text" name="password" />
      </label>
      <input type="submit" value="submit" />
      <button>Forget?</button>
    </form>
  );
}

export default Login;
