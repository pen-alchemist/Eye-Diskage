 import React, { useEffect, useState } from 'react';
 import { Link, useNavigate, useLocation } from 'react-router-dom';
 import './MainStyle.css';
 import logo from './logo.png'
 import axios from 'axios';

 axios.defaults.xsrfCookieName = 'csrftoken';
 axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

 const API_URL = process.env.REACT_APP_API_URL || '';

 const Main = ({ authStatus }) => {
  const navigate = useNavigate();
    const location = useLocation();
    const [data, setData] = useState({
        key: ''
    });

const fetchData = async () => {
        try {
            const response = await axios.get(`${API_URL}/api/eye_diskage/generate/`, {
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

  return (
    <div className="home-container">
      <header className="header">
            <img src={logo} />
            <h2 id="main-header2"> Eye-Diskage: Django Secret Key Generator Project </h2>
      </header>

      <main className="main">
        <section className="hero">
            <h1>Your Secret Key</h1>
            <h3 className="post-short">{data.key}</h3>
            <nav>
                <button className="one" onClick={() => fetchData()}>Refresh</button>
                <button className="zero" onClick={() => {navigator.clipboard.writeText(data.key)}}>Copy</button>
            </nav>
        </section>
      </main>

      <footer className="footer">
        <p><a href="https://docs.djangoproject.com/en/5.1/" target="_blank">Official Docs Django</a></p>
        <p><a href="https://github.com/pen-alchemist/Eye-Diskage" target="_blank">Source Code</a></p>
        <p>&copy; 2025 by Yehor Romanov aka @pen-alchemist </p>
      </footer>
    </div>
  );
};

 export default Main;