# transformer.py

class PokemonTransformer:
    def transform(self, data):
        simple_list = []

        for p in data:
            simple_list.append({
                "name": p["name"],
                "abilities": [a["ability"]["name"] for a in p["abilities"]]
            })

        return simple_list
