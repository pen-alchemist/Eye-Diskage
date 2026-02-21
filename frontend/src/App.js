import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Main from './components/MainPage';
import Django from './components/DjangoPage';
import RandomNumberPage from './components/RandomNumberPage'
import CaesarCipherPage from './components/CaesarPage';
import VigenereCipherPage from './components/VigenerePage';
import Auth from './components/Auth';

import { ThemeProvider } from './ThemeContext';
import GlobalLayout from './GlobalLayout';

function App() {
  const [auth, authStatus] = useState({
    isAuthenticated: false
  });

  return (
    <ThemeProvider>
      <Router>
        <GlobalLayout>
          <Routes>
            <Route path="/" element={<Main authStatus={authStatus} />} />
            <Route path="/main" element={<Main authStatus={authStatus} />} />
            <Route path="/django" element={<Django authStatus={authStatus} />} />
            <Route path="/random/numbers" element={<RandomNumberPage authStatus={authStatus} />} />
            <Route path="/caesar" element={<CaesarCipherPage authStatus={authStatus} />} />
            <Route path="/vigenere" element={<VigenereCipherPage authStatus={authStatus} />} />
          </Routes>
        </GlobalLayout>
      </Router>
    </ThemeProvider>
  );
}

export default App