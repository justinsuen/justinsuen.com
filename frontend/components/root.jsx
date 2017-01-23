import React from 'react';
import {Provider} from 'react-redux';

// react router
import {Router, Route, IndexRoute, hashHistory} from 'react-router';

// react components
import App from './app';

class Root extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Provider store={this.props.store}>
        <Router history={hashHistory}>
          <Route path="/" component={App} />
        </Router>
      </Provider>
    );
  }
}

export default Root;
