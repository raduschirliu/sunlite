import Nav from '../../components/Nav/Nav';
import Settings from '../../components/Settings/Settings';
import Sunrise from '../../components/Sunrise/Sunrise';
import './Account.css';

const Account = () => {
  return (
    <div className="account-page">
      <Nav />
      <div className="account-items">
        <Sunrise />
        <Settings />
      </div>
    </div>
  );
};

export default Account;
