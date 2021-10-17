import { useAuth0 } from '@auth0/auth0-react';
import { Button, TextField, CircularProgress, Snackbar } from '@mui/material';
import SettingsIcon from '@mui/icons-material/Settings';
import axios from 'axios';
import { useState } from 'react';
import './Settings.css';

const API_URL = process.env.REACT_APP_API_URL;

const Settings = () => {
  const { getAccessTokenSilently } = useAuth0();
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [phoneNumber, setPhoneNumber] = useState('');
  const [apiKey, setAPIKey] = useState('');

  const submit = () => {
    if (loading) return;

    setLoading(true);

    getAccessTokenSilently()
      .then((token) => {
        axios
          .post(
            `${API_URL}/account`,
            {
              api_key: apiKey,
              phone_number: phoneNumber,
            },
            { headers: { Authorization: `Bearer ${token}` } }
          )
          .then(() => setSnackbarOpen(true))
          .catch((err) => console.log(err))
          .finally(() => setLoading(false));
      })
      .catch((err) => {
        console.log(err);
        setLoading(false);
      });
  };

  return (
    <div className="settings-container">
      <div className="settings-title-container">
        <SettingsIcon />
        <p className="settings-title">Settings</p>
      </div>
      <TextField
        label="Phone Number"
        variant="outlined"
        onChange={(e) => setPhoneNumber(e.target.value)}
      />
      <TextField
        label="API Key"
        variant="outlined"
        onChange={(e) => setAPIKey(e.target.value)}
      />
      {loading ? (
        <CircularProgress />
      ) : (
        <Button variant="outlined" onClick={submit}>
          Update
        </Button>
      )}
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={3000}
        onClose={() => setSnackbarOpen(false)}
        message="Settings updated"
      />
    </div>
  );
};

export default Settings;
