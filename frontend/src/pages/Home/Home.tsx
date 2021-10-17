import { Link } from 'react-router-dom';
import logo from '../../assets/logo.svg';
import sun from '../../assets/sun.svg';
import './Home.css';

const Home = () => {
  return (
    <>
      <div className="home-page">
        <img className="home-logo" src={logo} alt="Logo" />
        <div style={{ backgroundImage: `url(${sun})` }} className="home-sun">
          <div className="home-account-container">
            <Link to="/account" className="home-account">
              Sign Up or Login
            </Link>
          </div>
        </div>
      </div>
      <div className="home-story">
        <p className="home-story-title">Our Story</p>
        <p className="home-story-desc">
          We all know how tough it can be to wake up before the sun is up, but
          did you know that there are health benefits associated with rising
          with the sun? Research has shown that syncing your wake and sleep
          cycle with the sun can result in less grogginess, easier wake-ups, and
          higher productivity. SunLite allows you to do this every day- even on
          dark winter mornings!
        </p>
      </div>
    </>
  );
};

export default Home;
