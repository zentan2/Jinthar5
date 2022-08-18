import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login/login'
import Markets from './pages/Markets/markets';
import Portfolio from './pages/Portfolio/portfolio';
import BSTest from './pages/BSTest/bstest';
import Example2 from './pages/Example2/example2';
import AddRemove from './pages/AddRemove/addremove';
//import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/markets" element={<Markets />} />
      <Route path="/portfolio" element={<Portfolio />} />
      <Route path="/BSTest" element={<BSTest />} />
      <Route path="/example2" element={<Example2 />} />
      <Route path="/addremove" element={<AddRemove />} />
      </Routes>
    </Router>
  );



}

export default App;