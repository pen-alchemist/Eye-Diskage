import React, { useState } from 'react';
import axios from 'axios';
import './VigenereStyle.css';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const API_URL = process.env.REACT_APP_API_URL || '';

const VigenereCipherPage = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [key, setKey] = useState('');
  const [mode, setMode] = useState('encrypt');
  const [loading, setLoading] = useState(false);

  const handleEncrypt = async () => {
    if (!text.trim()) {
      setError('ERR_INPUT: Data packet empty. Please enter text.');
      return;
    }

    if (!key.trim()) {
      setError('ERR_KEY: Vigenère matrix key is required.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post(
        `${API_URL}/api/eye_diskage/vigenere-cipher/`,
        { text, key, mode },
        { headers: { 'Content-Type': 'application/json' } }
      );

      if (response.status === 200) {
        setResult(response.data.result);
      }
    } catch (err) {
      if (err.response && err.response.status === 400) {
        setError(err.response.data.error);
      } else {
        setError('ERR_CONNECTION: Uplink failed. Please try again.');
      }
      setResult('');
    }
    setLoading(false);
  };

  return (
    <div className="page-container">
      <div className="glass-panel module-container">
        <div className="module-header">
          <h2 className="glitch-text" data-text="VIGENERE_CIPHER">VIGENERE_CIPHER</h2>
          <span className="status-badge">MATRIX_ALIGNED</span>
        </div>

        <div className="module-body flex-layout">
          <div className="controls-panel">
            <h3 className="panel-title">INPUT_STREAM</h3>

            <textarea
              className="cyber-textarea"
              placeholder="Enter text payload..."
              value={text}
              onChange={(e) => setText(e.target.value)}
              rows={4}
            />

            <div className="flex-row">
              <div className="cyber-input-group flex-2">
                <label>CIPHER_KEY (TEXT)</label>
                <input
                  type="text"
                  value={key}
                  onChange={(e) => setKey(e.target.value)}
                  placeholder="Enter key..."
                />
              </div>

              <div className="cyber-input-group flex-1">
                <label>OP_MODE</label>
                <select value={mode} onChange={(e) => setMode(e.target.value)}>
                  <option value="encrypt">ENCRYPT</option>
                  <option value="decrypt">DECRYPT</option>
                </select>
              </div>
            </div>

            <button className="btn-cyber w-100 mt-2" onClick={handleEncrypt} disabled={loading}>
              {loading ? 'PROCESSING_MATRIX...' : 'EXECUTE_OP'}
            </button>

            {error && <div className="error-box mt-3">{error}</div>}
          </div>

          <div className="output-panel">
            <h3 className="panel-title">OUTPUT_STREAM</h3>

            <textarea
              className="cyber-textarea result-readonly"
              readOnly
              value={result || 'AWAITING_DATA...'}
              rows={6}
            />

            {result && (
              <button
                className="btn-cyber outline mt-3 w-100"
                onClick={() => navigator.clipboard.writeText(result)}
              >
                COPY_BUFFER
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default VigenereCipherPage;
