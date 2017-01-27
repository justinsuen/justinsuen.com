import React from 'react';
import { withRouter } from 'react-router';

class Project extends React.Component {
  render() {
    return(
      <div className="project-container">
        <h1>Project</h1>
      </div>
    );
  }
}

export default withRouter(Project);
