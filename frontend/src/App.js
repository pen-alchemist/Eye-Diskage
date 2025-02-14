import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Main from './components/MainPage';
import CaesarCipherPage from './components/CaesarPage';
import VigenereCipherPage from './components/VigenerePage';
import MobileMain from './components/mobile/MobileMainPage'
import MobileCaesarCipherPage from './components/mobile/MobileCaesarPage'
import MobileVigenereCipherPage from './components/mobile/MobileVigenerePage'
import Auth from './components/Auth';

function App() {
  const [auth, authStatus] = useState({
        isAuthenticated: false
  });

  const [windowDimension, setWindowDimension] = useState(null);

  useEffect(() => {
    setWindowDimension(window.innerWidth);
  }, []);

  useEffect(() => {
    function handleResize() {
      setWindowDimension(window.innerWidth);
    }

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const isMobile = windowDimension <= 640;

  return (
    <Router>
        {isMobile ? (
          <>
          <Routes>
            <Route path="/" element={<MobileMain authStatus={authStatus} />} />
            <Route path="/main" element={<MobileMain authStatus={authStatus} />} />
            <Route path="/caesar" element={<MobileCaesarCipherPage authStatus={authStatus} />} />
            <Route path="/vigenere" element={<MobileVigenereCipherPage authStatus={authStatus} />} />
          </Routes>
          </>
        ) : (
          <>
          <Routes>
            <Route path="/" element={<Main authStatus={authStatus} />} />
            <Route path="/main" element={<Main authStatus={authStatus} />} />
            <Route path="/caesar" element={<CaesarCipherPage authStatus={authStatus} />} />
            <Route path="/vigenere" element={<VigenereCipherPage authStatus={authStatus} />} />
          </Routes>
          </>
        )}
    </Router>
  );
}

export default App