import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import CssBaseline from "@material-ui/core/CssBaseline";
import HelloWorld from "./HelloWorld";
import Home from "./Home";

function App() {
  return (
    <Router>
      <div>
        <CssBaseline />

        {/* Please please please don't edit this for content, just make new files for them please. */}
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/testing">
            <p>testing ayylmao</p>
            <HelloWorld />
          </Route>
          <Route path="/about">
            <p>about ayylmao</p>
            <HelloWorld />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
