import React, { useEffect, useState } from 'react';
 import { Link, useNavigate, useLocation } from 'react-router-dom';
import './MobileCaesarPage.css'; // Mobile-specific CSS
import logo from '../logo.png'
 import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

const API_URL = process.env.REACT_APP_API_URL || '';

function MobileVigenereCipherPage({ authStatus }) {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [shift, setShift] = useState(3); // Default shift value
  const [mode, setMode] = useState('encrypt'); // Default mode is 'encrypt'

  const handleEncrypt = async () => {
    if (!text.trim()) {
      setError('Please enter some text.');
      return;
    }

    try {
      const response = await axios.post(
        `${API_URL}/api/eye_diskage/vigenere-cipher/`,
        { text, shift, mode },
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );

      if (response.status === 200) {
        setResult(response.data.result); // Set the result from the response
        setError('');
      }
    } catch (err) {
      if (err.response && err.response.status === 400) {
        setError(err.response.data.error); // Display error message from the backend
      } else {
        setError('An error occurred. Please try again.');
      }
      setResult('');
    }
  };

  return (
    <div className="home-container">
      <header className="header">
        <img src={logo} alt="logo" />
        <h2 id="main-header2"> Eye-Diskage: Vigenère Cipher Encryption/Decryption </h2>
      </header>
      <header className="header2">
        <nav className="header-nav">
          <a href="/main">Django Secret Key Gen</a>
          <a href="/caesar">Caesar Cipher</a>
          <a href="/vigenere">Vigenère Cipher</a>
        </nav>
      </header>

      <main className="main">
        <section className="hero">
          <h1>Encrypt/Decrypt Your Text</h1>
          <textarea
            placeholder="Enter text to encrypt/decrypt..."
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows={5}
            cols={50}
          />
          {error && <p className="error-message">{error}</p>}

          <div className="controls">
            <label>
              Key:
              <input
                type="text"
                value={key}
                onChange={(e) => setKey(e.target.value)}
                placeholder="Enter key..."
              />
            </label>

            <label>
              Mode:
              <select value={mode} onChange={(e) => setMode(e.target.value)}>
                <option value="encrypt">Encrypt</option>
                <option value="decrypt">Decrypt</option>
              </select>
            </label>
          </div>

          <nav>
            <button className="vigenere-one" onClick={handleEncrypt}>
              {mode === 'encrypt' ? 'Encrypt' : 'Decrypt'}
            </button>
            <button className="vigenere-zero" onClick={() => navigator.clipboard.writeText(result)}>
              Copy Result
            </button>
          </nav>

          {result && (
            <div className="result-container">
              <h3>{mode === 'encrypt' ? 'Encrypted Text:' : 'Decrypted Text:'}</h3>
              <textarea
                readOnly
                value={result}
                rows={5}
                cols={50}
                className="result-textarea"
              />
            </div>
          )}
        </section>
      </main>

      <footer className="vigenere-footer">
        <p>&copy; 2025 by Yehor Romanov aka @pen-alchemist </p>
      </footer>
    </div>
  );
};

export default MobileVigenereCipherPage;