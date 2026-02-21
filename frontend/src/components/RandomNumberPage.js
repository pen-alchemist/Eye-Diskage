import React, { useState } from 'react';
import axios from 'axios';
import './RandomStyle.css';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const API_URL = process.env.REACT_APP_API_URL || '';

const RandomNumberPage = () => {
  const [minValue, setMinValue] = useState(1);
  const [maxValue, setMaxValue] = useState(100);
  const [count, setCount] = useState(1);
  const [unique, setUnique] = useState(true);
  const [randomNumbers, setRandomNumbers] = useState([]);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (minValue >= maxValue) {
      setError('ERR_BOUNDS: min_value must be less than max_value.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post(
        `${API_URL}/api/eye_diskage/secure-random-numbers/`,
        { min_value: minValue, max_value: maxValue, count, unique },
        { headers: { 'Content-Type': 'application/json' } }
      );

      if (response.status === 200) {
        setRandomNumbers(response.data.random_numbers);
      }
    } catch (err) {
      if (err.response && err.response.status === 400) {
        setError(err.response.data.error);
      } else {
        setError('ERR_CONNECTION: An error occurred communicating with the generator node.');
      }
      setRandomNumbers([]);
    }
    setLoading(false);
  };

  return (
    <div className="page-container">
      <div className="glass-panel module-container">
        <div className="module-header">
          <h2 className="glitch-text" data-text="RNG_CORE">RNG_CORE</h2>
          <span className="status-badge">ENTROPY_SYNCED</span>
        </div>

        <div className="module-body flex-layout">
          <div className="controls-panel">
            <h3 className="panel-title">PARAMETERS</h3>

            <div className="cyber-input-group">
              <label>MIN_VAL</label>
              <input type="number" value={minValue} onChange={(e) => setMinValue(parseInt(e.target.value) || 0)} />
            </div>

            <div className="cyber-input-group">
              <label>MAX_VAL</label>
              <input type="number" value={maxValue} onChange={(e) => setMaxValue(parseInt(e.target.value) || 0)} />
            </div>

            <div className="cyber-input-group">
              <label>ITERATIONS</label>
              <input type="number" value={count} onChange={(e) => setCount(parseInt(e.target.value) || 1)} />
            </div>

            <div className="cyber-input-group">
              <label>UNIQUE_CONSTRAINT</label>
              <select value={unique} onChange={(e) => setUnique(e.target.value === 'true')}>
                <option value={true}>ENABLED / YES</option>
                <option value={false}>DISABLED / NO</option>
              </select>
            </div>

            <button className="btn-cyber w-100 mt-2" onClick={handleGenerate} disabled={loading}>
              {loading ? 'CALCULATING_ENTROPY...' : 'INITIALIZE_RNG'}
            </button>

            {error && <div className="error-box mt-3">{error}</div>}
          </div>

          <div className="output-panel">
            <h3 className="panel-title">DATA_OUTPUT</h3>
            <div className="result-matrix">
              {randomNumbers.length > 0 ? (
                <div className="matrix-numbers">
                  {randomNumbers.map((num, idx) => (
                    <span key={idx} className="matrix-num">{num}</span>
                  ))}
                </div>
              ) : (
                <div className="waiting-text">AWAITING_INITIALIZATION...</div>
              )}
            </div>

            {randomNumbers.length > 0 && (
              <button
                className="btn-cyber outline mt-3 w-100"
                onClick={() => navigator.clipboard.writeText(randomNumbers.join(', '))}
              >
                COPY_DATA_STREAM
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default RandomNumberPage;
