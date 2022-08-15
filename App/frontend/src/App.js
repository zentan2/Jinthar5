import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login/login'
import Markets from './pages/Markets/markets';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/markets" element={<Markets />} />

      </Routes>
    </Router>
  );



}

export default App;