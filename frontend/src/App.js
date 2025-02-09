import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Main from './components/MainPage';
import ReadPost from './components/ReadPostPage';
import About from './components/AboutPage';
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
        <Routes>
            <Route path="/main" element={<Main authStatus={authStatus} />} />
            <Route path="/blog/post/:slug" element={<ReadPost authStatus={authStatus} />} />
            <Route path="/about" element={<About authStatus={authStatus} />} />
            <Route path="/" element={<Navigate replace to="/main" />} />
        </Routes>
    </Router>
  );
}

export default App