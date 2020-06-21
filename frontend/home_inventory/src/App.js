import React from "react";
import "./App.css";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  BrowserRouter,
} from "react-router-dom";
import ItemDetail from "../src/component/itemDetail";
import Items from "../src/component/items";
import Login from "../src/component/login";
import Register from "../src/component/register";

function App() {
  return (
    <BrowserRouter>
      <Router>
        <Switch>
          <Route path="/item/:key" children={<ItemDetail />} />
          <Route path="/items">
            <Items></Items>
          </Route>
          <Route path="/login" children={<Login />} />
          <Route path="/register" children={<Register />} />
          <Route path="/">
            <h1>Home inventory</h1>
            <button>Login</button>
            <button>Register</button>
          </Route>
        </Switch>
      </Router>
    </BrowserRouter>
  );
}

export default App;
