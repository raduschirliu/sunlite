import { useAuth0 } from '@auth0/auth0-react';

const Account = () => {
  const { logout } = useAuth0();

  return (
    <div>
      <p>Your account!</p>
      <button onClick={() => logout()}>Logout</button>
    </div>
  );
};

export default Account;
