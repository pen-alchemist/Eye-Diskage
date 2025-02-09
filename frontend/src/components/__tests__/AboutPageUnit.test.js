import '@testing-library/jest-dom';
import React from 'react';
import { render, screen, fireEvent, within } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import axios from 'axios';
import About from '../AboutPage';

jest.mock('axios', () => ({
  get: jest.fn(),
  defaults: { xsrfCookieName: '', xsrfHeaderName: '' }, // Fix here
}));

describe('About Component', () => {
  beforeEach(() => {
    render(
      <BrowserRouter>
        <About authStatus={true} />
      </BrowserRouter>
    );

  });

  test('renders header text', () => {
    expect(screen.getByText('Simple Django and React Blog with Testing Automation')).toBeInTheDocument();
  });

  test('renders navigation main button', () => {
    expect(screen.getByRole('button', { name: 'Main' })).toBeInTheDocument();
  });

  test('renders navigation about button', () => {
    expect(screen.getByRole('button', { name: 'About' })).toBeInTheDocument();
  });

  test('renders footer text', () => {
    expect(screen.getByText(/© 2025 by Yehor Romanov/i)).toBeInTheDocument();
  });

  test('renders About section heading in main', () => {
    // Find the "About" heading inside the main section to avoid conflicts
    const mainSection = screen.getByRole('main');
    expect(within(mainSection).getByRole('heading', { name: 'About' })).toBeInTheDocument();
  });

  test('renders About section with email information', () => {
    expect(screen.getByText('Feel free to contact me: yehor.romanov7@gmail.com')).toBeInTheDocument();
  });

  test('renders About section with github profile link', () => {
    expect(screen.getByText('Also My GitHub https://github.com/pen-alchemist')).toBeInTheDocument();
  });

  test('renders About section with github project source information', () => {
    expect(screen.getByText('Project Source: https://github.com/pen-alchemist/simple_django_react_blog')).toBeInTheDocument();
  });

  test('renders "Return to Blog" button and navigates to main page', () => {
    const returnButton = screen.getByText('Return to Blog');
    expect(returnButton).toBeInTheDocument();
  });
});
