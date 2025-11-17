import json

class JSONExporter:
    def export(self, data, filename="pokemon.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("JSON file saved:", filename)
