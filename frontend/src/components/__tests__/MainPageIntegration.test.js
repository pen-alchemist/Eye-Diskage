import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import Main from '../MainPage';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';

const mock = jest.mock('axios', () => ({
  get: jest.fn(),
  defaults: { xsrfCookieName: '', xsrfHeaderName: '' }, // Fix here
}));

const mockDataPage1 = {
  posts: [
    {
      post_content_short: 'First post content',
      post_slug: 'first-post',
      post_date: '2023-10-01',
      post_image: '/images/first-post.jpg',
    },
  ],
  is_next: true,
  is_previous: false,
  current: 1,
  pages_count: 2,
  posts_count: 2,
};

const mockDataPage2 = {
  posts: [
    {
      post_content_short: 'Second post content',
      post_slug: 'second-post',
      post_date: '2023-10-02',
      post_image: '/images/second-post.jpg',
    },
  ],
  is_next: false,
  is_previous: true,
  current: 2,
  pages_count: 2,
  posts_count: 2,
};

describe('Main Component Integration Tests', () => {
  beforeEach(() => {
    mock.reset();

    render(
      <Router>
        <Main authStatus={true} />
      </Router>
    );
  });

  test('navigates to the about page when "About" button is clicked', () => {
    // Click the "About" button
    fireEvent.click(screen.getByText('About'));

    // Verify navigation to the main page
    expect(window.location.pathname).toBe('/main');
  });

  test('navigates to the blog page when "Main" button is clicked after "About" button', () => {
    // Click the "About" button
    fireEvent.click(screen.getByText('About'));
    // Click the "Main" button
    fireEvent.click(screen.getByText('Main'));

    // Verify navigation to the main page
    expect(window.location.pathname).toBe('/main');
  });

  test('fetches posts on initial render', async () => {
    mock.onGet('/blog/api/blog/all/').reply(200, mockDataPage1);

    await waitFor(() => {
      expect(mock.history.get.length).toBe(1); // Verify API call was made
    });
  });

  test('fetches posts for page 1 on initial render', async () => {
    mock.onGet('/blog/api/blog/all/').reply(200, mockDataPage1);

    await waitFor(() => {
      expect(mock.history.get[0].params.page).toBe(1); // Verify initial page is 1
    });
  });

  test('navigates to the next page when "Next" button is clicked', async () => {
    mock.onGet('/blog/api/blog/all/').replyOnce(200, mockDataPage1); // Initial load
    mock.onGet('/blog/api/blog/all/').replyOnce(200, mockDataPage2); // Next page

    fireEvent.click(screen.getByText('Next')); // Click "Next" button

    await waitFor(() => {
      expect(mock.history.get.length).toBe(2); // Verify second API call
    });
  });

  test('requests page 2 when "Next" button is clicked', async () => {
    mock.onGet('/blog/api/blog/all/').replyOnce(200, mockDataPage1); // Initial load
    mock.onGet('/blog/api/blog/all/').replyOnce(200, mockDataPage2); // Next page

    fireEvent.click(screen.getByText('Next')); // Click "Next" button

    await waitFor(() => {
      expect(mock.history.get[1].params.page).toBe(2); // Verify page 2 was requested
    });
  });

  test('navigates to the previous page when "Previous" button is clicked', async () => {
    mock.onGet('/blog/api/blog/all/').replyOnce(200, mockDataPage2); // Initial load (page 2)
    mock.onGet('/blog/api/blog/all/').replyOnce(200, mockDataPage1); // Previous page

    fireEvent.click(screen.getByText('Previous')); // Click "Previous" button

    await waitFor(() => {
      expect(mock.history.get.length).toBe(2); // Verify second API call
    });
  });

  test('requests page 1 when "Previous" button is clicked', async () => {
    mock.onGet('/blog/api/blog/all/').replyOnce(200, mockDataPage2); // Initial load (page 2)
    mock.onGet('/blog/api/blog/all/').replyOnce(200, mockDataPage1); // Previous page

    fireEvent.click(screen.getByText('Previous')); // Click "Previous" button

    await waitFor(() => {
      expect(mock.history.get[1].params.page).toBe(1); // Verify page 1 was requested
    });
  });

  test('disables "Previous" button on the first page', async () => {
    mock.onGet('/blog/api/blog/all/').reply(200, mockDataPage1);

    await waitFor(() => {
      const previousButton = screen.getByText('Previous').closest('button');
      expect(previousButton).toBeDisabled(); // Verify "Previous" button is disabled
    });
  });

  test('disables "Next" button on the last page', async () => {
    mock.onGet('/blog/api/blog/all/').reply(200, {
      ...mockDataPage2,
      is_next: false, // No next page
    });

    await waitFor(() => {
      const nextButton = screen.getByText('Next').closest('button');
      expect(nextButton).toBeDisabled(); // Verify "Next" button is disabled
    });
  });

  test('handles API error gracefully', async () => {
    mock.onGet('/blog/api/blog/all/').reply(500); // Simulate API error

    await waitFor(() => {
      expect(mock.history.get.length).toBe(1); // Verify API call was made
    });
  });
});