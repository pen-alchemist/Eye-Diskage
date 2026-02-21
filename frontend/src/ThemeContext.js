import React, { createContext, useState, useContext, useEffect } from 'react';

const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
    // Try to load from localStorage first, otherwise fallback
    const [theme, setTheme] = useState(localStorage.getItem('theme') || 'dark');
    const [pill, setPill] = useState(localStorage.getItem('pill') || 'blue'); // 'red' or 'blue'

    useEffect(() => {
        localStorage.setItem('theme', theme);
        const root = document.documentElement;
        if (theme === 'dark') {
            root.classList.add('dark-theme');
            root.classList.remove('light-theme');
        } else {
            root.classList.add('light-theme');
            root.classList.remove('dark-theme');
        }
    }, [theme]);

    useEffect(() => {
        localStorage.setItem('pill', pill);
        const root = document.documentElement;
        if (pill === 'red') {
            root.classList.add('pill-red');
            root.classList.remove('pill-blue');
        } else {
            root.classList.add('pill-blue');
            root.classList.remove('pill-red');
        }
    }, [pill]);

    const toggleTheme = () => setTheme((prev) => (prev === 'dark' ? 'light' : 'dark'));
    const togglePill = () => setPill((prev) => (prev === 'blue' ? 'red' : 'blue'));

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme, pill, togglePill }}>
            {children}
        </ThemeContext.Provider>
    );
};

export const useTheme = () => useContext(ThemeContext);
