import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8080/api",
});

// Ingredients
export const addIngredient = (data) => API.post("/ingredients", data);
export const getIngredients = () => API.get("/ingredients");

// Recipes
export const addRecipe = (data) => API.post("/recipes", data);
export const getRecipes = () => API.get("/recipes");

// Preferences
export const addPreference = (data) => API.post("/preferences", data);
export const getPreferences = () => API.get("/preferences");

// Meal Planner
export const getMealPlan = () => API.get("/planner");

// AI Suggestions
export const getSuggestions = () => API.get("/suggestions");

export default API;
