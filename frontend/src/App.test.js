import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders app and ThemeProvider', () => {
  render(<App />);
  const linkElement = screen.getByText(/CYBERPUNK TIMELINE/i);
  expect(linkElement).toBeInTheDocument();
});
