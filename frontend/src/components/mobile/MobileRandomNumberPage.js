import React, { useState } from 'react';
import axios from 'axios';
import './MobileCaesarPage.css'; // Mobile-specific CSS
import logo from '../logo.png'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const API_URL = process.env.REACT_APP_API_URL || ''; // Update with your Django backend URL

const MobileRandomNumberPage = () => {
  const [minValue, setMinValue] = useState(1);
  const [maxValue, setMaxValue] = useState(100);
  const [count, setCount] = useState(1);
  const [unique, setUnique] = useState(true);
  const [randomNumbers, setRandomNumbers] = useState([]);
  const [error, setError] = useState('');

  const handleGenerate = async () => {
    if (minValue >= maxValue) {
      setError('min_value must be less than max_value.');
      return;
    }

    try {
      const response = await axios.post(
        `${API_URL}/api/eye_diskage/secure-random-numbers/`,
        { min_value: minValue, max_value: maxValue, count, unique },
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );

      if (response.status === 200) {
        setRandomNumbers(response.data.random_numbers); // Set the random numbers from the response
        setError('');
      }
    } catch (err) {
      if (err.response && err.response.status === 400) {
        setError(err.response.data.error); // Display error message from the backend
      } else {
        setError('An error occurred. Please try again.');
      }
      setRandomNumbers([]);
    }
  };

  return (
    <div className="home-container">
      <header className="header">
        <img src={logo} alt="logo" />
        <h2 id="main-header2"> Eye-Diskage: Random Number Generator </h2>
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

      <main className="main">
        <section className="hero">
          <h1>Generate Secure Random Numbers</h1>

          <div className="controls">
            <label>
              Min Value:
              <input
                type="number"
                value={minValue}
                onChange={(e) => setMinValue(parseInt(e.target.value))}
              />
            </label>

            <label>
              Max Value:
              <input
                type="number"
                value={maxValue}
                onChange={(e) => setMaxValue(parseInt(e.target.value))}
              />
            </label>

            <label>
              Count:
              <input
                type="number"
                value={count}
                onChange={(e) => setCount(parseInt(e.target.value))}
              />
            </label>

            <label>
              Unique:
              <select
                value={unique}
                onChange={(e) => setUnique(e.target.value === 'true')}
              >
                <option value={true}>Yes</option>
                <option value={false}>No</option>
              </select>
            </label>
          </div>

          {error && <p className="error-message">{error}</p>}

          <nav>
            <button className="caesar-one" onClick={handleGenerate}>
              Generate
            </button>
            <button
              className="caesar-zero"
              onClick={() => navigator.clipboard.writeText(randomNumbers.join(', '))}
            >
              Copy Result
            </button>
          </nav>

          {randomNumbers.length > 0 && (
            <div className="result-container">
              <h3>Generated Random Numbers:</h3>
              <textarea
                readOnly
                value={randomNumbers.join(', ')}
                rows={5}
                cols={50}
                className="result-textarea"
              />
            </div>
          )}
        </section>
      </main>

      <footer className="caesar-footer">
        <p>&copy; 2025 by Yehor Romanov aka @pen-alchemist </p>
      </footer>
    </div>
  );
};

export default MobileRandomNumberPage;