
import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Ustaw zmienną środowiskową REACT_APP_CODESPACE_NAME jeśli jest dostępna w window
if (!process.env.REACT_APP_CODESPACE_NAME && window && window.location) {
  const host = window.location.host;
  const match = host.match(/^([^.]+)-8000\.app\.github\.dev/);
  if (match) {
    process.env.REACT_APP_CODESPACE_NAME = match[1];
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
