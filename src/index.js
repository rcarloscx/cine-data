//DEFAULT
import React from 'react';
import ReactDOM from 'react-dom/client';
//PRIMEFLEX, PRIMEREACT CORE AND CSS
import 'primeflex/primeflex.css';
import "primereact/resources/themes/lara-light-indigo/theme.css";  //theme
import "primereact/resources/primereact.min.css";                  //core css
import "primeicons/primeicons.css";                                //icons
//WebPage
import WebPage from './WebPage';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <WebPage />
  </React.StrictMode>
);
