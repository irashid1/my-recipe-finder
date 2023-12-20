import React, { useState } from "react";
import axios from "axios";

const SearchBar = ({ setRecipes }) => {
  const [query, setQuery] = useState("");

  const searchRecipes = async () => {
    try {
      const response = await axios.get(
        `http://localhost:5000/api/recipes?query=${query}`
      );
      setRecipes(response.data);
    } catch (error) {
      console.error("Error fetching recipes:", error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={searchRecipes}>Search</button>
    </div>
  );
};

export default SearchBar;
