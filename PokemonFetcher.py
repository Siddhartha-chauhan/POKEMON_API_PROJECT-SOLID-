import requests

class PokemonFetcher:
    def fetch_first_25(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=25"
        response = requests.get(url).json()

        pokemon_data = []
        for item in response["results"]:
            details = requests.get(item["url"]).json()
            pokemon_data.append(details)

        return pokemon_data
