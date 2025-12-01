import { useState } from "react";
import { getMealPlan } from "../api/api";

export default function Planner() {
  const [plan, setPlan] = useState([]);

  const loadPlan = async () => {
    const res = await getMealPlan();
    setPlan(res.data);
  };

  return (
    <div>
      <h2>Weekly Meal Planner</h2>

      <button onClick={loadPlan}>Generate Plan</button>

      <div className="card">
        <ul>
          {plan.map((p, i) => (
            <li key={i}>{p}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
