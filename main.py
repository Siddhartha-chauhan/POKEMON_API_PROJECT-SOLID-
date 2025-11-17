from PokemonFetcher import PokemonFetcher
from PokemonTransformer import PokemonTransformer
from csv_exporter import CSVExporter
from TXTExporter import TXTExporter
from PDFExporter import PDFExporter
from JSONExporter import JSONExporter

def main():
    fetcher = PokemonFetcher()
    transformer = PokemonTransformer()

    print("Fetching Pokémon...")
    raw = fetcher.fetch_first_25()
 # <-- your function name was wrong

    print("Transforming Pokémon data...")
    clean = transformer.transform(raw)

    # PRINT DATA ON TERMINAL
    print("\n--- Pokémon Data ---")
    for p in clean:
        print(f"Name: {p['name']}")
        print(f"Abilities: {', '.join(p['abilities'])}")
        print("----------------------")

    # SAVE TO FILES
    print("\nSaving files...")
    CSVExporter().export(clean)
    TXTExporter().export(clean)
    PDFExporter().export(clean)
    JSONExporter().export(clean)  # <-- NOW clean exists

    print("Done!")

if __name__ == "__main__":
    main()
