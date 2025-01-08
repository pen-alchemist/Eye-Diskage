 import React, { useEffect, useState } from 'react';
 import { Link, useNavigate, useLocation, useParams } from 'react-router-dom';
 import './ReadBlogStyle.css';
 import logo from './logo.png'
 import axios from 'axios';

 axios.defaults.xsrfCookieName = 'csrftoken';
 axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

 const API_URL = process.env.REACT_APP_API_URL || '';

 const ReadBlog = ({ authStatus }) => {
  const { slug } = useParams();
  const [data, setData] = useState({
      post_title: '',
      post_content: '',
      post_date: '',
      post_image: ''
  });

const fetchData = async () => {
  try {
    const response = await axios.get(`${API_URL}/blog/api/blog/read/${slug}/`, {
      headers: {
        'Content-Type': 'application/json'
      },
    });
    const { post_title, post_content, post_date, post_image } = response.data;
    setData({
        post_title,
        post_content,
        post_date,
        post_image
    });
  } catch (error) {
  }
};

    useEffect(() => {
        fetchData();
    }, [slug]);

    const handlePageChange = (newPage) => {
        fetchData(newPage);
    };

  return (
    <div className="home-container">
      <header className="header">
        <p>
            <img style={{ width: "20%", height: "10%", display: "block", marginLeft: "auto", marginRight: "auto" }} src={logo} />
        </p>
        <h1>Read Blog Post</h1>
        <nav>
          <ul>
            <li><a href="/blog">Blog</a></li>
            <li><a href="/about">About</a></li>
          </ul>
        </nav>
      </header>

      <main className="main">
        <section className="hero">
          <h2> Simple Django and React Blog with Testing Automation  </h2>
        </section>

        <h2> Posts </h2>
        <section className="posts">
          <div className="parent">
            <div className="content">
                {data.data && (
                <>
                    <h3 className="post-short">{data.data.post_content}</h3>
                    <h3 className="post-date">{data.data.post_date}</h3>
                    <img
                        className="post-image"
                        src={`${API_URL}${data.data.post_image}`}
                        alt="Post Image about post"
                    />
                </>
                )}
            </div>
          </div>
        </section>

        <p>
        <div className="pagination">
            <a href="/blog" target="_blank" target="_self">
                <button className="nav-button_pages">
                    <i className="button-icon bi-arrow-left"></i>
                    <span>Return to Blog</span>
                </button>
            </a>
        </div>
        </p>
      </main>

      <footer className="footer">
        <p>&copy; 2025 by Yehor Romanov @wwwinri aka @pen-alchemist </p>
      </footer>
    </div>
  );
};

 export default ReadBlog;