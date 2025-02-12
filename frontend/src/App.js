import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Main from './components/MainPage';
import MobileMain from './components/mobile/MobileMainPage'
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
          </Routes>
          </>
        ) : (
          <>
          <Routes>
            <Route path="/" element={<Main authStatus={authStatus} />} />
            <Route path="/main" element={<Main authStatus={authStatus} />} />
          </Routes>
          </>
        )}
    </Router>
  );
}

export default App