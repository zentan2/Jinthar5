import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login/login'
import Markets from './pages/Markets/markets';
import Portfolio from './pages/Portfolio/portfolio';
import BSTest from './pages/BSTest/bstest';
import Example from './pages/Example/example';
//import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/markets" element={<Markets />} />
      <Route path="/portfolio" element={<Portfolio />} />
      <Route path="/BSTest" element={<BSTest />} />
      </Routes>
    </Router>
  );



}

export default App;