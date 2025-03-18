import React, { useState } from "react";
import { motion } from "framer-motion";
import "./RandomPokemon.css";

// ✅ タイプごとのカラー設定（日本語）
const typeColors = {
  ノーマル: "#A8A77A",
  ほのお: "#EE8130",
  みず: "#6390F0",
  でんき: "#F7D02C",
  くさ: "#7AC74C",
  こおり: "#96D9D6",
  かくとう: "#C22E28",
  どく: "#A33EA1",
  じめん: "#E2BF65",
  ひこう: "#A98FF3",
  エスパー: "#F95587",
  むし: "#A6B91A",
  いわ: "#B6A136",
  ゴースト: "#735797",
  ドラゴン: "#6F35FC",
  あく: "#705746",
  はがね: "#B7B7CE",
  フェアリー: "#D685AD"
};

const RandomPokemon = () => {
  const [pokemon, setPokemon] = useState(null); // ✅ 初期値を `null` にする
  const [loading, setLoading] = useState(false);

  const fetchRandomPokemon = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/random_pokemon/");
      const data = await response.json();
      setPokemon(data);
      console.log("取得したポケモンデータ:", data); // ✅ デバッグ用
    } catch (error) {
      console.error("エラーが発生しました:", error);
    }
    setLoading(false);
  };

  return (
    <div className="pokemon-container">
      <motion.button 
        className="fetch-button"
        onClick={fetchRandomPokemon}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
      >
        Let's go meet Pokemon !
      </motion.button>

      {loading && <p>Loading...</p>}

      {/* ✅ `pokemon` が `null` でない場合にのみ表示する */}
      {pokemon && (
        <motion.div 
          className="pokemon-card"
          initial={{ opacity: 0, scale: 0.5 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5 }}
          style={{ borderColor: typeColors[pokemon.type?.split(", ")[0] || "ノーマル"] }}
        >
          <h2>{pokemon.name}</h2>
          <img src={pokemon.image_url} alt={pokemon.name} className="pokemon-image" />

          {/* ✅ タイプを2つ表示する */}
          <div className="pokemon-types">
            {pokemon.type?.split(", ").map((t, index) => (
              <span key={index} className="pokemon-type" style={{ backgroundColor: typeColors[t] || "#A8A77A" }}>
                {t}
              </span>
            ))}
          </div>
        </motion.div>
      )}
    </div>
  );
};



export default RandomPokemon;
