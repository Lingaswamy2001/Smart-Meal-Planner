import { useState } from "react";
import { addPreference } from "../api/api";

export default function Preferences() {
  const [diet, setDiet] = useState("");

  const save = async () => {
    await addPreference({ diet });
    setDiet("");
  };

  return (
    <div>
      <h2>Preferences</h2>

      <div className="card">
        <select value={diet} onChange={(e) => setDiet(e.target.value)}>
          <option value="">Select Diet Type</option>
          <option value="veg">Veg</option>
          <option value="non-veg">Non-Veg</option>
          <option value="vegan">Vegan</option>
        </select>

        <button onClick={save}>Save Preference</button>
      </div>
    </div>
  );
}
