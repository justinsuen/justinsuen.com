import React from 'react';
import { withRouter } from 'react-router';

// components
import Splash from './splash';
import Project from './project';
import Contact from './contact';

class Home extends React.Component {
  render() {
    return(
      <div className="home-container">
        <Splash/>
        <Project/>
        <Contact/>
      </div>
    );
  }
}

export default withRouter(Home);
