import { Link } from 'react-router-dom';
import logo from '../../assets/logo.svg';
import sun from '../../assets/sun.svg';
import './Home.css';

const Home = () => {
  return (
    <div className="home-page">
      <img className="home-logo" src={logo} alt="Logo" />
      {/* <img src={sun} alt="Sun" /> */}
      <div style={{ backgroundImage: `url(${sun})` }} className="home-sun">
        <div className="home-account-container">
          <Link to="/account" className="home-account">
            Sign Up or Login
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;
