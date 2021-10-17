import WbSunnyIcon from '@mui/icons-material/WbSunny';
import { Button, Snackbar, TextField } from '@mui/material';
import { useState } from 'react';
import './Sunrise.css';

const Sunrise = () => {
  const [, setSunriseTime] = useState('');
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const hasSunrise = false;

  const setSunrise = () => {
    setSnackbarOpen(true);
  };

  return (
    <div className="sunrise-container">
      <div className="sunrise-title-container">
        <WbSunnyIcon />
        <p className="sunrise-title">My Sunrise</p>
      </div>
      <div className="sunrise-time">
        {hasSunrise ? (
          <div className="sunrise-time-digits">
            <p className="sunrise-time-digit">0</p>
            <p className="sunrise-time-digit">8</p>
            <p className="sunrise-time-separator">:</p>
            <p className="sunrise-time-digit">2</p>
            <p className="sunrise-time-digit">3</p>
          </div>
        ) : (
          <div className="sunrise-unset">
            <p>Text +1 (825) 801-5267 to set your sunrise, or set one below</p>
            <div className="sunrise-set-container">
              <TextField
                label="Sunrise Time"
                variant="outlined"
                onChange={(e) => setSunriseTime(e.target.value)}
              />
              <Button variant="outlined" onClick={setSunrise}>
                Set
              </Button>
            </div>
          </div>
        )}
      </div>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={3000}
        onClose={() => setSnackbarOpen(false)}
        message="Sunrise set"
      />
    </div>
  );
};

export default Sunrise;
