import React from 'react';
import { withRouter } from 'react-router';

class Project extends React.Component {
  render() {
    return(
      <section className="project-container">
        <h1>Project</h1>
      </section>
    );
  }
}

export default withRouter(Project);
