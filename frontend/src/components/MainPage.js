 import React, { useEffect, useState } from 'react';
 import { Link, useNavigate, useLocation } from 'react-router-dom';
 import './MainStyle.css';
 import logo from './logo.png'
 import axios from 'axios';

 axios.defaults.xsrfCookieName = 'csrftoken';
 axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

 const API_URL = process.env.REACT_APP_API_URL || '';

 const Main = ({ authStatus }) => {
  const navigate = useNavigate();
    const location = useLocation();
    const [data, setData] = useState({
        posts: [],
        is_next: false,
        is_previous: false,
        current: 1,
        pages_count: 1,
        posts_count: 0
    });

const fetchData = async (page = 1) => {
        try {
            const response = await axios.get(`${API_URL}/blog/api/blog/all/`, {
                headers: {
                    'Content-Type': 'application/json'
                },
                params: {
                    page: page
                }
            });
            const { posts, is_next, is_previous, current, pages_count, posts_count } = response.data;
            setData({
                posts,
                is_next,
                is_previous,
                current,
                pages_count,
                posts_count
            });
        } catch (error) {}
    };

    useEffect(() => {
        const page = data.current_page
        fetchData(page);
    }, [navigate, location]);

    const handlePageChange = (newPage) => {
        fetchData(newPage);
    };

  return (
    <div className="home-container">
      <header className="header">
            <img src={logo} />
            <h2> Simple Django and React Blog with Testing Automation  </h2>
        <nav>
            <button className="nav-button_pages"><Link to="/main">Blog</Link></button>
            <button className="nav-button_pages"><Link to="/about">About</Link></button>
        </nav>
      </header>

      <main className="main">
        <section className="hero">
            <h1>All Blogs</h1>
        </section>
        <section className="posts">
            <div className="parent">
                <div className="content">
                    {data.posts_count > 0 ? (
                        <>
                        <ul className="posts-list">
                            {data.posts.map(({ post_content_short, post_slug, post_date, post_image }) => (
                            <>
                                <Link to={`/blog/post/${post_slug}`} className="post-link">
                                    <h3 className="post-short">{post_content_short}</h3>
                                </Link>
                                <h3 className="post-date">{post_date}</h3>
                                <img className="post-image"
                                    src={`${API_URL}${post_image}`}
                                alt="Post Image about post" />
                            </>
                            ))}
                        </ul>
                        </>
                    ) : (
                        <h1><p className="no-posts">There are no posts!</p></h1>
                    )}
                </div>
            </div>
        </section>

        <p>
        <div className="pagination">
          <button className="nav-button_pages" onClick={() => handlePageChange(data.current - 1)} disabled={!data.is_previous}>
            <i className="button-icon bi-arrow-left"></i>
            <span>Previous</span>
          </button>
          <span>Page {data.current} of {data.pages_count}</span>
          <button className="nav-button_pages" onClick={() => handlePageChange(data.current + 1)} disabled={!data.is_next}>
            <span>Next</span>
            <i className="button-icon bi-arrow-right"></i>
          </button>
        </div>
        </p>
      </main>

      <footer className="footer">
        <p>&copy; 2025 by Yehor Romanov @wwwinri aka @pen-alchemist </p>
      </footer>
    </div>
  );
};

 export default Main;