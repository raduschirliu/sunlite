import { withAuthenticationRequired } from '@auth0/auth0-react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Account from '../../pages/Account/Account';
import Home from '../../pages/Home/Home';
import './App.css';

const GuardedRoute = ({ component, ...rest }: any) => {
  return <Route component={withAuthenticationRequired(component)} {...rest} />;
};

const App = () => {
  return (
    <div className="app-container">
      <Router>
        <Switch>
          <GuardedRoute path="/account" component={Account} />
          <Route path="/" component={Home} exact />
        </Switch>
      </Router>
    </div>
  );
};

export default App;
