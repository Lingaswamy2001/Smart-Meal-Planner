import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Login from './components/Login';
import Home from './components/Home';
import Ingredients from './components/Ingredients';
import Recipes from './components/Recipes';
import Preferences from './components/Preferences';
import Planner from './components/Planner';
import Suggestions from './components/Suggestions';

function App() {
  const [user, setUser] = useState(null); // login state

  return (
    <>
      <Navbar user={user} setUser={setUser} />
      <Routes>
        <Route path="/" element={user ? <Home /> : <Login setUser={setUser} />} />
        <Route path="/ingredients" element={<Ingredients />} />
        <Route path="/recipes" element={<Recipes />} />
        <Route path="/preferences" element={<Preferences />} />
        <Route path="/planner" element={<Planner />} />
        <Route path="/suggestions" element={<Suggestions />} />
      </Routes>
    </>
  );
}

export default App;
