import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

function Navbar({ user, setUser }) {
  const navigate = useNavigate(); // ✅ get navigate function

  const handleLogout = () => {
    setUser(null);      // clear user state
    navigate('/');       // ✅ redirect to login page
  };

  return (
    <nav className="navbar">
      <div>
        <Link to="/">Home</Link>
        <Link to="/ingredients">Ingredients</Link>
        <Link to="/recipes">Recipes</Link>
        <Link to="/suggestions">Suggestions</Link>
        <Link to="/preferences">Preferences</Link>
        <Link to="/planner">Planner</Link>
      </div>
      <div>
        {user ? (
          <>
            <span>Welcome, {user}</span>
            <button onClick={handleLogout}>Logout</button>
          </>
        ) : (
          <Link to="/">Login</Link>
        )}
      </div>
    </nav>
  );
}

export default Navbar;
