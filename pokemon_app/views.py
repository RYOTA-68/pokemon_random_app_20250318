from django.http import JsonResponse
import random
from .models import Pokemon

# ✅ ポケモンの一覧を取得する API
def pokemon_list(request):
    pokemons = Pokemon.objects.all().values("id", "name_jp", "type", "image_url")  # ✅ `name` → `name_jp` に変更
    return JsonResponse({"pokemons": list(pokemons)})

# ✅ ランダムなポケモンを取得する API
def random_pokemon(request):
    pokemon_count = Pokemon.objects.count()
    if pokemon_count == 0:
        return JsonResponse({"error": "No Pokémon found"}, status=404)

    random_index = random.randint(1, pokemon_count)
    random_pokemon = Pokemon.objects.get(id=random_index)

    return JsonResponse({
        "id": random_pokemon.id,
        "name": random_pokemon.name_jp,  # ✅ `name` → `name_jp` に変更
        "type": random_pokemon.type,  # ✅ 日本語のタイプ
        "image_url": random_pokemon.image_url
    })
