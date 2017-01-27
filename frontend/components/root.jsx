import React from 'react';
import {Provider} from 'react-redux';

// react router
import {Router, Route, IndexRoute, browserHistory} from 'react-router';

// react components
import App from './app';
import Home from './home';

class Root extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Provider store={this.props.store}>
        <Router history={browserHistory}>
          <Route path="/" component={App}>
            <IndexRoute component={Home} />
          </Route>
        </Router>
      </Provider>
    );
  }
}

export default Root;
