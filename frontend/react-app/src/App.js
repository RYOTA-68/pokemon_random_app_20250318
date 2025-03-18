// src/App.js

import React from 'react';
import './App.css';
import RandomPokemon from './components/RandomPokemon';

function App() {
  return (
    <div className="App">
      <h1>ポケモンランダム表示</h1>
      <RandomPokemon />
    </div>
  );
}

export default App;
