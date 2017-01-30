import React from 'react';
import { withRouter } from 'react-router';

class Splash extends React.Component {
  render() {
    return(
      <section className="splash-container">
        <h1>Hi, I'm Justin Suen</h1>
        <div className="hline"></div>
        <h3>Software Engineer with a strong interest in Data Science and Visualization.</h3>
        <h3>Recent Mathematics graduate from UC Berkeley.</h3>
        <h3>I build visual software to teach and make life easier.</h3>
      </section>
    );
  }
}

export default withRouter(Splash);
