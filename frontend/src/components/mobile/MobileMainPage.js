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

const fetchData = async () => {
        try {
            const response = await axios(`${API_URL}/api/eye_diskage/django-ker-generate/`, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const { key } = response.data;
            setData({
                key
            });
        } catch (error) {}
    };

useEffect(() => {
        fetchData();
    }, [navigate, location]);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="mobile-home-container">
      <header className="header">
            <img src={logo} />
            <h2 id="main-header2"> Eye-Diskage: Django Secret Key Generator </h2>
      </header>
      <header className="header2">
        <nav className="header-nav">
          <a href="/main">Django Secret Key Gen</a>
          <a href="/caesar">Caesar Cipher</a>
          <a href="/vigenere">Vigenère Cipher</a>
        </nav>
      </header>

      <main className="mobile-main">
        <section className="mobile-hero">
            <h1>Your Secret Key</h1>
            <h3 className="mobile-post-short">{data.key}</h3>
            <nav>
                <button className="mobile-one" onClick={() => fetchData()}>Refresh</button>
                <button className="mobile-zero" onClick={() => {navigator.clipboard.writeText(data.key)}}>Copy</button>
            </nav>
        </section>
      </main>

      <footer className="mobile-footer">
        <p><a href="https://docs.djangoproject.com/en/5.1/" target="_blank">Official Docs Django</a></p>
        <p><a href="https://github.com/pen-alchemist/Eye-Diskage" target="_blank">Source Code</a></p>
        <p>&copy; 2025 by Yehor Romanov aka @pen-alchemist </p>
      </footer>
    </div>
  );
};

 export default MobileMain;