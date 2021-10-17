import { useAuth0 } from '@auth0/auth0-react';
import { useEffect } from 'react';

const Account = () => {
  const { logout, getAccessTokenSilently } = useAuth0();

  useEffect(() => {
    getAccessTokenSilently()
      .then((token) => {
        console.log(token);
      })
      .catch((err) => console.log(err));
  });

  return (
    <div>
      <p>Your account!</p>
      <button onClick={() => logout()}>Logout</button>
    </div>
  );
};

export default Account;
