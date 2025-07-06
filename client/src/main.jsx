// Importing Modules/Packages
import { createRoot } from 'react-dom/client';
import { StrictMode } from 'react';
import App from './App.jsx';

// Importing Stylesheets
import './assets/output/main.min.css';

// if ('serviceWorker' in navigator) {
//   try {
//     await navigator.serviceWorker.register('/sw.js');
//   }
//   catch (error) {
//     console.error('Service Worker not registered: ', error);
//     throw error;
//   }
// }

createRoot(document.getElementById('root')).render(<StrictMode><App /></StrictMode>);