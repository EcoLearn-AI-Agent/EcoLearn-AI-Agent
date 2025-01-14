import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
  return (
    <div className="home">
      <h1>Welcome to EcoLearn</h1>
      <p>Learn about the environment and earn Memecoins!</p>
      <div className="home-buttons">
        <Link to="/tasks" className="btn">Start Learning</Link>
        <Link to="/rewards" className="btn">Check Rewards</Link>
      </div>
    </div>
  );
};

export default Home;
