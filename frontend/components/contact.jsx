import React from 'react';
import { withRouter } from 'react-router';

class Contact extends React.Component {
  render() {
    return(
      <section className="contact-container">
        <h1>Contact</h1>
      </section>
    );
  }
}

export default withRouter(Contact);
