import React from 'react';
import { withRouter } from 'react-router';

class Contact extends React.Component {
  render() {
    return(
      <div className="contact-container">
        <h1>Contact</h1>
      </div>
    );
  }
}

export default withRouter(Contact);
