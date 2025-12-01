import { useState } from "react";
import { getSuggestions } from "../api/api";

export default function Suggestions() {
  const [suggestions, setSuggestions] = useState([]);

  const fetch = async () => {
    const res = await getSuggestions();
    setSuggestions(res.data);
  };

  return (
    <div>
      <h2>AI Meal Suggestions</h2>

      <button onClick={fetch}>Get Suggestions</button>

      <div className="card">
        <ul>
          {suggestions.map((s, i) => (
            <li key={i}>{s}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
