import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App/App';
import reportWebVitals from './reportWebVitals';
import { Auth0Provider } from '@auth0/auth0-react';
// import history from './history';
import './index.css';

const AUTH0_DOMAIN = 'dev-4nutzf54.us.auth0.com';
const AUTH0_CLIENT_ID = 'FMdMIzOua71jIMXH5QPcZGpmVEceRhKV';

// const onRedirectCallback = (appState: any) => {
//   // Use the router's history module to replace the url
//   history.replace(appState?.returnTo || window.location.pathname);
// };

ReactDOM.render(
  <React.StrictMode>
    <Auth0Provider
      domain={AUTH0_DOMAIN}
      clientId={AUTH0_CLIENT_ID}
      redirectUri={window.location.origin}
    >
      <App />
    </Auth0Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
