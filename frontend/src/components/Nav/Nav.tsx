import { useAuth0 } from '@auth0/auth0-react';
import lamp from '../../assets/lamp.png';
import './Nav.css';

const Nav = () => {
  const { user, logout } = useAuth0();

  return (
    <div className="nav-container">
      <img src={lamp} alt="Lamp Logo" />
      <p className="nav-welcome">
        Welcome, <span className="nav-welcome-name">{user?.name}</span>
      </p>
      <p className="nav-logout" onClick={() => logout()}>
        Logout
      </p>
    </div>
  );
};

export default Nav;
