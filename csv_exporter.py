# csv_exporter.py
import csv

class CSVExporter:
    def export(self, data, filename="pokemon.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Abilities"])

            for p in data:
                writer.writerow([p["name"], ";".join(p["abilities"])])

        print("CSV file saved:", filename)
