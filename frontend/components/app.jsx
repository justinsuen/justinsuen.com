import React from 'react';
import { withRouter } from 'react-router';

class App extends React.Component {
  render() {
    return(
      <div className="app-container">
        <h1>Hello World!</h1>
      </div>
    );
  }
}

export default withRouter(App);
