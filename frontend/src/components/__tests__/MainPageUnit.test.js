import '@testing-library/jest-dom';
import React from 'react';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import axios from 'axios';
import Main from '../MainPage';

jest.mock('axios', () => ({
  get: jest.fn(),
  defaults: { xsrfCookieName: '', xsrfHeaderName: '' }, // Fix here
}));

describe('Main Component', () => {
  const mockPosts = {
    data: {
      posts: [
        {
          post_content_short: 'Test Post 1',
          post_slug: 'test-post-1',
          post_date: '2025-02-09',
          post_image: '/images/test1.jpg',
        },
        {
          post_content_short: 'Test Post 2',
          post_slug: 'test-post-2',
          post_date: '2025-02-08',
          post_image: '/images/test2.jpg',
        },
      ],
      is_next: true,
      is_previous: false,
      current: 1,
      pages_count: 3,
      posts_count: 2,
    },
  };

  beforeEach(() => {
    axios.get.mockResolvedValue(mockPosts);
  });

  test('renders header, navigation, and footer', async () => {
    render(
      <BrowserRouter>
        <Main authStatus={true} />
      </BrowserRouter>
    );

    expect(screen.getByText('Simple Django and React Blog with Testing Automation')).toBeInTheDocument();
    expect(screen.getByText('Blog')).toBeInTheDocument();
    expect(screen.getByText('About')).toBeInTheDocument();
    expect(screen.getByText(/© 2025 by Yehor Romanov/i)).toBeInTheDocument();
  });

  test('fetches and displays blog posts', async () => {
    render(
      <BrowserRouter>
        <Main authStatus={true} />
      </BrowserRouter>
    );

    await waitFor(() => {
      expect(screen.getByText('Test Post 1')).toBeInTheDocument();
      expect(screen.getByText('Test Post 2')).toBeInTheDocument();
    });
  });

  test('shows pagination and handles next page', async () => {
    render(
      <BrowserRouter>
        <Main authStatus={true} />
      </BrowserRouter>
    );

    await waitFor(() => {
      expect(screen.getByText('Page 1 of 3')).toBeInTheDocument();
    });

    const nextButton = screen.getByText('Next');
    expect(nextButton).not.toBeDisabled();

    fireEvent.click(nextButton);

    await waitFor(() => {
      expect(axios.get).toHaveBeenCalledWith(expect.stringContaining('/blog/api/blog/all/'), expect.any(Object));
    });
  });

  test('shows message when no posts exist', async () => {
    axios.get.mockResolvedValueOnce({
      data: {
        posts: [],
        is_next: false,
        is_previous: false,
        current: 1,
        pages_count: 1,
        posts_count: 0,
      },
    });

    render(
      <BrowserRouter>
        <Main authStatus={true} />
      </BrowserRouter>
    );

    await waitFor(() => {
      expect(screen.getByText('There are no posts!')).toBeInTheDocument();
    });
  });
});
