import { useState, useEffect } from "react";
import { addIngredient, getIngredients } from "../api/api";

export default function Ingredients() {
  const [name, setName] = useState("");
  const [list, setList] = useState([]);

  useEffect(() => {
    load();
  }, []);

  const load = async () => {
    const res = await getIngredients();
    setList(res.data);
  };

  const save = async () => {
    await addIngredient({ name });
    setName("");
    load();
  };

  return (
    <div>
      <h2>Ingredients</h2>

      <div className="card">
        <input
          type="text"
          placeholder="Enter ingredient"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <button onClick={save}>Add Ingredient</button>
      </div>

      <div className="card">
        <h3>Available Ingredients</h3>
        <ul>
          {list.map((i) => (
            <li key={i.id}>{i.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
