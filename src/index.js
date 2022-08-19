//DEFAULT
import React from 'react';
import ReactDOM from 'react-dom/client';
//CSS
import 'bootstrap/dist/css/bootstrap.min.css';
//WebPage
import WebPage from './WebPage';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <WebPage />
  </React.StrictMode>
);
