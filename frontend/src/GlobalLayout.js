import React from 'react';
import { useTheme } from './ThemeContext';
import { Link } from 'react-router-dom';
import './GlobalLayout.css';

const GlobalLayout = ({ children }) => {
    const { theme, toggleTheme, pill, togglePill } = useTheme();

    return (
        <div className="layout-container">
            <header className="glass-panel nav-header">
                <div className="logo-area">
                    <Link to="/">[ EYE_DISKAGE ]</Link>
                </div>
                <nav className="nav-links">
                    <Link to="/django">Django_Secret_Key</Link>
                    <Link to="/random/numbers">Number_Generator</Link>
                    <Link to="/caesar">Caesar_Shift</Link>
                    <Link to="/vigenere">Vigenere_Cipher</Link>
                </nav>
                <div className="controls">
                    <button
                        className={`theme-toggle ${theme === 'dark' ? 'blue-pill' : 'red-pill'}`}
                        onClick={toggleTheme}
                    >
                        {theme === 'dark' ? '🔵 BLUE PILL' : '🔴 RED PILL'}
                    </button>
                    <button
                        className={`pill-toggle ${pill}`}
                        onClick={togglePill}
                    >
                        {pill === 'red' ? 'Magician' : 'Fool'}
                    </button>
                </div>
            </header>

            <main className="content-area">
                {children}
            </main>

            <footer className="footer glass-panel">
                <p>CERN x MATRIX // CYBERPUNK TIMELINE</p>
            </footer>
        </div>
    );
};

export default GlobalLayout;
