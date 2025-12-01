import { useState } from "react";
import { addRecipe } from "../api/api";

export default function Recipes() {
  const [title, setTitle] = useState("");
  const [ingredients, setIngredients] = useState("");
  const [cuisine, setCuisine] = useState("");
  const [instructions, setInstructions] = useState("");

  const save = async () => {
    await addRecipe({
      title,
      ingredients: ingredients.split(","),
      cuisine,
      instructions,
    });

    setTitle("");
    setIngredients("");
    setCuisine("");
    setInstructions("");
  };

  return (
    <div>
      <h2>Recipes</h2>

      <div className="card">
        <input
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <input
          placeholder="Ingredients (comma separated)"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
        />

        <input
          placeholder="Cuisine"
          value={cuisine}
          onChange={(e) => setCuisine(e.target.value)}
        />

        <textarea
          placeholder="Instructions"
          value={instructions}
          onChange={(e) => setInstructions(e.target.value)}
        />

        <button onClick={save}>Add Recipe</button>
      </div>
    </div>
  );
}
