import React from 'react';
import { withRouter } from 'react-router';

class Splash extends React.Component {
  render() {
    return(
      <div className="splash-container">
        <h1>Splash</h1>
      </div>
    );
  }
}

export default withRouter(Splash);
