from django.urls import path
from .views import pokemon_list, random_pokemon  # ✅ 両方の関数をインポート

urlpatterns = [
    path("pokemon/", pokemon_list, name="pokemon_list"),  # ✅ ポケモン一覧API
    path("random_pokemon/", random_pokemon, name="random_pokemon"),  # ✅ ランダムポケモンAPI
]
