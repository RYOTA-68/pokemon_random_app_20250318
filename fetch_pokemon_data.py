import requests
import mysql.connector

# MySQL接続設定
db = mysql.connector.connect(
    host="localhost",
    user="RYOTA",
    password="Komainu___608",
    database="pokemon_db",
    charset="utf8mb4"
)
cursor = db.cursor()

# 英語のタイプを日本語に変換する辞書
TYPE_TRANSLATION = {
    "normal": "ノーマル",
    "fire": "ほのお",
    "water": "みず",
    "electric": "でんき",
    "grass": "くさ",
    "ice": "こおり",
    "fighting": "かくとう",
    "poison": "どく",
    "ground": "じめん",
    "flying": "ひこう",
    "psychic": "エスパー",
    "bug": "むし",
    "rock": "いわ",
    "ghost": "ゴースト",
    "dragon": "ドラゴン",
    "dark": "あく",
    "steel": "はがね",
    "fairy": "フェアリー"
}

# PokeAPI からポケモン情報を取得
def fetch_pokemon_data():
    for i in range(1, 1025):  # 1025匹まで取得（PokéAPIの最新データに応じて調整）
        url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{i}/"
        url_species = f"https://pokeapi.co/api/v2/pokemon-species/{i}/"

        response_pokemon = requests.get(url_pokemon)
        response_species = requests.get(url_species)

        if response_pokemon.status_code == 200 and response_species.status_code == 200:
            data_pokemon = response_pokemon.json()
            data_species = response_species.json()

            # 🔹 日本語名を取得
            jp_name = next((name["name"] for name in data_species["names"] if name["language"]["name"] == "ja"), None)

            # 🔹 英語のタイプを取得し、日本語に変換
            type_english = [t["type"]["name"] for t in data_pokemon["types"]]
            type_japanese = ", ".join([TYPE_TRANSLATION.get(t, t) for t in type_english])

            # 🔹 画像URLを取得
            image_url = data_pokemon["sprites"]["front_default"]

            # 🔹 データベースに登録
            cursor.execute("""
                INSERT INTO pokemon (id, name_jp, type, image_url) 
                VALUES (%s, %s, %s, %s) 
                ON DUPLICATE KEY UPDATE name_jp=%s, type=%s, image_url=%s
            """, (i, jp_name, type_japanese, image_url, jp_name, type_japanese, image_url))

    db.commit()
    cursor.close()
    db.close()

fetch_pokemon_data()
