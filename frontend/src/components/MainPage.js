import React from 'react';
import './MainStyle.css';

const Main = () => {
  return (
    <div className="home-container">
      <section className="hero glass-panel">
        <h1 className="glitch" data-text="EYE DISKAGE">EYE DISKAGE</h1>
        <h2 className="subtitle">System Init // Cryptography Meets QA Automation</h2>

        <div className="terminal-window">
          <div className="terminal-header">
            <span className="dot red"></span>
            <span className="dot yellow"></span>
            <span className="dot green"></span>
            <span className="title">root@pen-alchemist:~</span>
          </div>
          <div className="terminal-body">
            <p><span className="prompt">$</span> ./init_eye.sh</p>
            <p className="output">Starting EYE DISKAGE platform...</p>
            <p className="output">Loading cryptographic modules [OK]</p>
            <p className="output">Establishing secure connection [OK]</p>
            <p className="output">Running all tests... [OK]</p>
            <p className="output">[DONE!]</p>
            <p className="output">EYE DISKAGE is a transparent, open-source platform built to demonstrate Cryptographic Systems and QA Automation.</p>
            <p><span className="prompt">$</span> cat mission.txt</p>
            <p className="output">Whether you are exploring secure protocols or validating complex workflows, EYE provides the tools to observe, test, and trust.</p>
            <p className="output animated-typing">Understand. Test. Trust.<span className="cursor">_</span></p>
          </div>
        </div>

        <div className="action-buttons">
          <a href="/django" className="btn-cyber block-btn">ACCESS MODULES</a>
          <a href="https://colyte.pro/" target="_blank" rel="noreferrer" className="btn-cyber block-btn outline">EXTERNAL LINK: COLYTE</a>
        </div>
      </section>
    </div>
  );
};

export default Main;
