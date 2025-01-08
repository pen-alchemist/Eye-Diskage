import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Blog from './components/Blog';
import ReadBlog from './components/ReadBlog';
import About from './components/About';
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
            <Route path="/blog" element={<Blog authStatus={authStatus} />} />
            <Route path="/blog/post/:slug" element={<ReadBlog authStatus={authStatus} />} />
            <Route path="/about" element={<About authStatus={authStatus} />} />
            <Route path="/" element={<Navigate replace to="/blog" />} />
        </Routes>
    </Router>
  );
}

export default App