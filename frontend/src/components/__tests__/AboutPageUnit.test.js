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
  test('renders header, navigation, and footer', () => {
    render(
      <BrowserRouter>
        <About authStatus={true} />
      </BrowserRouter>
    );

    expect(screen.getByText('Simple Django and React Blog with Testing Automation')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Blog' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'About' })).toBeInTheDocument();
    expect(screen.getByText(/© 2025 by Yehor Romanov/i)).toBeInTheDocument();
  });

  test('renders About section with contact information', () => {
    render(
      <BrowserRouter>
        <About authStatus={true} />
      </BrowserRouter>
    );

    // Find the "About" heading inside the main section to avoid conflicts
    const mainSection = screen.getByRole('main');
    expect(within(mainSection).getByRole('heading', { name: 'About' })).toBeInTheDocument();

    expect(screen.getByText('Feel free to contact me: yehor.romanov7@gmail.com')).toBeInTheDocument();
    expect(screen.getByText('Also My GitHub https://github.com/pen-alchemist')).toBeInTheDocument();
    expect(screen.getByText('Project Source: https://github.com/pen-alchemist/simple_django_react_blog')).toBeInTheDocument();
  });

  test('renders "Return to Blog" button and navigates to main page', () => {
    render(
      <BrowserRouter>
        <About authStatus={true} />
      </BrowserRouter>
    );

    const returnButton = screen.getByText('Return to Blog');
    expect(returnButton).toBeInTheDocument();
    fireEvent.click(returnButton);
  });
});
