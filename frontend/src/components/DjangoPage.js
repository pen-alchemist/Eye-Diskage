import React, { useEffect, useState } from 'react';
import './DjangoStyle.css';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

const API_URL = process.env.REACT_APP_API_URL || '';

const DjangoPage = () => {
  const [data, setData] = useState({ key: '' });
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  const fetchData = async () => {
    setLoading(true);
    setCopied(false);
    try {
      const response = await axios(`${API_URL}/api/eye_diskage/django-ker-generate/`, {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        }
      });
      const { key } = response.data;
      setData({ key });
    } catch (error) {
      console.error(error);
      setData({ key: 'ERROR_GENERATING_KEY' });
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleCopy = () => {
    if (data.key) {
      navigator.clipboard.writeText(data.key);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  return (
    <div className="page-container">
      <div className="glass-panel module-container">
        <div className="module-header">
          <h2 className="glitch-text" data-text="DJANGO_KEY_GEN">DJANGO_KEY_GEN</h2>
          <span className="status-badge">SECURE_LEVEL_9</span>
        </div>

        <div className="module-body">
          <p className="instruction-text">Initiating cryptographic routine to generate a secure 50-character random string compliant with Django secret key specifications.</p>

          <div className="key-display-box">
            {loading ? (
              <span className="loading-text">GENERATING_HASH[.......]</span>
            ) : (
              <span className="key-text">{data.key}</span>
            )}
          </div>

          <div className="action-buttons mt-4">
            <button className="btn-cyber" onClick={fetchData} disabled={loading}>
              {loading ? 'PROCESSING...' : 'REGENERATE_KEY'}
            </button>
            <button className={`btn-cyber outline ${copied ? 'copied' : ''}`} onClick={handleCopy} disabled={!data.key || loading}>
              {copied ? 'COPIED_TO_CLIPBOARD' : 'COPY_KEY'}
            </button>
          </div>
        </div>
      </div>
      <div className="docs-link mt-4 text-center">
        <a href="https://docs.djangoproject.com/en/5.1/" target="_blank" rel="noreferrer" className="cyber-link">READ OFFICIAL DJANGO DOCS</a>
      </div>
    </div>
  );
};

export default DjangoPage;
