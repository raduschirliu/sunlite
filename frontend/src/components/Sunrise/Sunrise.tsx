import WbSunnyIcon from '@mui/icons-material/WbSunny';
import { Button, Snackbar, TextField } from '@mui/material';
import { useState } from 'react';
import './Sunrise.css';

const Sunrise = () => {
  const [sunriseTime, setSunriseTime] = useState('');
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [digits, setDigits] = useState<string[]>([]);

  const setSunrise = () => {
    if (sunriseTime.length === 5) {
      setDigits([
        sunriseTime.charAt(0),
        sunriseTime.charAt(1),
        sunriseTime.charAt(3),
        sunriseTime.charAt(4),
      ]);
    }

    setSnackbarOpen(true);
  };

  return (
    <div className="sunrise-container">
      <div className="sunrise-title-container">
        <WbSunnyIcon />
        <p className="sunrise-title">My Sunrise</p>
      </div>
      <div className="sunrise-time">
        {digits?.length === 4 ? (
          <>
            <div className="sunrise-time-digits">
              <p className="sunrise-time-digit">{digits[0]}</p>
              <p className="sunrise-time-digit">{digits[1]}</p>
              <p className="sunrise-time-separator">:</p>
              <p className="sunrise-time-digit">{digits[2]}</p>
              <p className="sunrise-time-digit">{digits[3]}</p>
            </div>
            <Button
              className="sunrise-time-clear"
              variant="outlined"
              onClick={() => setDigits([])}
            >
              Clear
            </Button>
          </>
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
