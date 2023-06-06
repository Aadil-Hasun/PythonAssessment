import requests
import pandas as pd
from requests.exceptions import ConnectionError


def download_data(url, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except ConnectionError:
            pass
    raise Exception("Failed to download data after multiple attempts")


def process_data(data):
    rows = []
    for pokemon in data['pokemon']:
        multipliers = pokemon.get('multipliers')
        if multipliers is None:
            multipliers = []
        row = {
            'id': pokemon['id'],
            'num': pokemon['num'],
            'name': pokemon['name'],
            'img': pokemon['img'],
            'type': ', '.join(pokemon['type']),
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'candy': pokemon.get('candy', ''),
            'candy_count': pokemon.get('candy_count', 0),
            'egg': pokemon.get('egg', ''),
            'spawn_chance': pokemon.get('spawn_chance', 0.0),
            'avg_spawns': pokemon.get('avg_spawns', 0),
            'spawn_time': pokemon.get('spawn_time', ''),
            'multipliers': ', '.join(str(m) for m in multipliers),
            'weakness': ', '.join(pokemon.get('weaknesses', []))
        }
        rows.append(row)
    return rows


url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
pokemon_data = download_data(url)

# Process the data into structured format
processed_data = process_data(pokemon_data)

# Export the data to Excel
df = pd.DataFrame(processed_data)
df.to_excel("poke_data.xlsx", index=False)