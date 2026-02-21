import React, { useState } from 'react';
import axios from 'axios';
import './CaesarStyle.css';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const API_URL = process.env.REACT_APP_API_URL || '';

const CaesarCipherPage = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [shift, setShift] = useState(3);
  const [mode, setMode] = useState('encrypt');
  const [loading, setLoading] = useState(false);

  const handleEncrypt = async () => {
    if (!text.trim()) {
      setError('ERR_INPUT: Data packet empty. Please enter text.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post(
        `${API_URL}/api/eye_diskage/caesar-cipher/`,
        { text, shift, mode },
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
          <h2 className="glitch-text" data-text="CAESAR_SHIFT">CAESAR_SHIFT</h2>
          <span className="status-badge">CIPHER_READY</span>
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
              <div className="cyber-input-group flex-1">
                <label>SHIFT_VAL</label>
                <select value={shift} onChange={(e) => setShift(parseInt(e.target.value))}>
                  {[...Array(26).keys()].map((value) => (
                    <option key={value} value={value}>{value}</option>
                  ))}
                </select>
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
              {loading ? 'PROCESSING_CIPHER...' : 'EXECUTE_OP'}
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

export default CaesarCipherPage;
