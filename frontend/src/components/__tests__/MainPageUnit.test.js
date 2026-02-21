import '@testing-library/jest-dom';
import React from 'react';
import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Main from '../MainPage';

describe('Main Component CYBERPUNK', () => {
  beforeEach(() => {
    // Mock window dimension if needed, but we removed the mobile split
    render(
      <BrowserRouter>
        <Main authStatus={true} />
      </BrowserRouter>
    );
  });

  test('renders glitch header text', () => {
    expect(screen.getByText('EYE OS')).toBeInTheDocument();
  });

  test('renders subtitle', () => {
    expect(screen.getByText('System Init // Cryptography Meets Automation')).toBeInTheDocument();
  });

  test('renders terminal window content', () => {
    expect(screen.getByText(/Establishing secure connection/i)).toBeInTheDocument();
    expect(screen.getByText(/Loading cryptographic modules/i)).toBeInTheDocument();
    expect(screen.getByText(/Understand\. Test\. Trust\./i)).toBeInTheDocument();
  });

  test('renders ACCESS MODULES button', () => {
    expect(screen.getByText('ACCESS MODULES')).toBeInTheDocument();
  });

  test('renders EXTERNAL LINK button', () => {
    expect(screen.getByText('EXTERNAL LINK: COLYTE')).toBeInTheDocument();
  });
});
