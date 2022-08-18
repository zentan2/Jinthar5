import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login/login'
import Markets from './pages/Markets/markets';
import Portfolio from './pages/Portfolio/portfolio';
import Navbar from './components/Navbar';
import AddRemove from './pages/AddRemove/addremove';
import SignUp from './pages/SignUp/signup';
function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/markets" element={<Markets />} />
      <Route path="/portfolio" element={<Portfolio />} />
      <Route path="/addremove" element={<AddRemove />} />
      <Route path="/signup" element={<SignUp />} />
      </Routes>
    </Router>
  );



}

export default App;