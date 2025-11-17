# txt_exporter.py

class TXTExporter:
    def export(self, data, filename="pokemon.txt"):
        with open(filename, "w") as f:
            for p in data:
               
                f.write(f"Name: {p['name']}\n")
                f.write(f"Abilities: {', '.join(p['abilities'])}\n\n")

        print("TXT file saved:", filename)
