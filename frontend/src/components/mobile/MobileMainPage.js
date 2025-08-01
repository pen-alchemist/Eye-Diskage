import React, { useEffect, useState } from 'react';
 import { Link, useNavigate, useLocation } from 'react-router-dom';
import './MobileMainPage.css'; // Mobile-specific CSS
import logo from '../logo.png'
 import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

const API_URL = process.env.REACT_APP_API_URL || '';

function MobileMain({ authStatus }) {
  const navigate = useNavigate();
  const location = useLocation();
  const [data, setData] = useState({
        key: ''
    });

useEffect(() => {
    }, [navigate, location]);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="mobile-home-container">
      <header className="header">
            <img src={logo} />
            <h2 id="main-header2"> Eye-Diskage: Welcome to our project! </h2>
      </header>
      <header className="header2">
        <nav className="header-nav">
          <a href="/main">Home Page</a>
          <a href="/django">Django Secret Key Gen</a>
          <a href="/random/numbers">Random Number Generator</a>
          <a href="/caesar">Caesar Cipher</a>
          <a href="/vigenere">Vigenère Cipher</a>
          <a href="https://colyte.pro/" target="_blank">Colyte</a>
        </nav>
      </header>

      <main className="mobile-main">
        <section className="mobile-hero">
            <h1>Welcome to EYE by Colyte</h1>
            <h3 className="post-short">Where cryptography meets automation.</h3>
            <h3 className="post-short">EYE is a transparent, open-source platform built to demonstrate cryptographic systems and streamline testing automation. Whether you are exploring secure protocols or validating complex workflows, EYE provides the tools to observe, test, and trust.</h3>
            <h3 className="post-short">Designed for developers, researchers, and cryptography enthusiasts, EYE makes it easy to interact with encryption processes while automating the verification behind them. See cryptography in action—clearly, securely, and reproducibly.</h3>
            <h3 className="post-short">Understand. Test. Trust.</h3>
        </section>
      </main>

      <footer className="mobile-footer">
        <p><a href="https://github.com/pen-alchemist/Eye-Diskage" target="_blank">Source Code</a></p>
        <p>&copy; 2025 by Yehor Romanov aka @pen-alchemist </p>
      </footer>
    </div>
  );
};

 export default MobileMain;