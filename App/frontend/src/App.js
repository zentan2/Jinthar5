import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login/login'
import Markets from './pages/Markets/markets';
import Portfolio from './pages/Portfolio/portfolio';
import Navbar from './components/Navbar';
import Testing from './pages/testing/Testing';

function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/markets" element={<Markets />} />
      <Route path="/portfolio" element={<Portfolio />} />
      </Routes>
    </Router>
  );



}

export default App;