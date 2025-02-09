import '@testing-library/jest-dom';
import React from 'react';
import { render, screen, fireEvent, within, queryByAttribute } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import axios from 'axios';
import About from '../AboutPage';

jest.mock('axios', () => ({
  get: jest.fn(),
  defaults: { xsrfCookieName: '', xsrfHeaderName: '' }, // Fix here
}));

describe('About Component Integration Tests', () => {
  beforeEach(() => {
    render(
      <BrowserRouter>
        <About authStatus={true} />
      </BrowserRouter>
    );
  });

  test('navigates to the main page when "Main" button is clicked', () => {
    // Click the "Main" button
    fireEvent.click(screen.getByText('Main'));

    // Verify navigation to the main page
    expect(window.location.pathname).toBe('/main');
  });

  test('navigates to the main page when "About" button is clicked after "Main" button', () => {
    // Click the "Main" button
    fireEvent.click(screen.getByText('Main'));
    // Click the "About" button
    fireEvent.click(screen.getAllByText('About')[0]);

    // Verify navigation to the main page
    expect(window.location.pathname).toBe('/about');
  });

  test('navigates to the main page when "Return to Blog" button is clicked', () => {
    // Click the "Return to Blog" button
    fireEvent.click(screen.getByText('Return to Blog'));

    // Verify navigation to the main page
    expect(window.location.pathname).toBe('/main');
  });
});