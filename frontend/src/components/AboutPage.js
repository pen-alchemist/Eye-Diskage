 import React, { useEffect, useState } from 'react';
 import { Link, useNavigate, useLocation, useParams } from 'react-router-dom';
 import './AboutStyle.css';
 import logo from './logo.png'
 import axios from 'axios';

 axios.defaults.xsrfCookieName = 'csrftoken';
 axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

 const API_URL = process.env.REACT_APP_API_URL || '';

 const About = ({ authStatus }) => {
  const { slug } = useParams();
  const [data, setData] = useState({
    data: [],
  });

    useEffect(() => {
        },
    );

    const handlePageChange = (newPage) => {
    };

  return (
    <div className="home-container">
      <header className="header">
            <img src={logo} />
            <h2 id="main-header2"> Simple Django and React Blog with Testing Automation  </h2>
        <nav>
            <button id="nav-button-blog" className="nav-button_pages"><Link to="/main">Main</Link></button>
            <button id="nav-button-about" className="nav-button_pages"><Link to="/about">About</Link></button>
        </nav>
      </header>

      <main className="main">
        <section className="hero">
          <h1>About</h1>
          <h3> Feel free to contact me: yehor.romanov7@gmail.com  </h3>
          <h3> Also My GitHub https://github.com/pen-alchemist </h3>
          <h3> Project Source: https://github.com/pen-alchemist/simple_django_react_blog </h3>
        </section>

        <p>
        <div className="pagination">
            <a href="/main" target="_blank" target="_self">
                <button className="nav-button_pages">
                    <i className="button-icon bi-arrow-left"></i>
                    <span>Return to Blog</span>
                </button>
            </a>
        </div>
        </p>
      </main>

      <footer className="footer">
        <p>&copy; 2025 by Yehor Romanov @wwwinri aka @pen-alchemist </p>
      </footer>
    </div>
  );
};

 export default About;