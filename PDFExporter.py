from fpdf import FPDF

class PDFExporter:
    def export(self, data, filename="pokemon.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Pokémon Report (Table Format)", ln=True)
        pdf.ln(5)

        # Table column widths
        col_id = 20
        col_name = 40
        col_abilities = 130   # wide because abilities list is long

        # Header row
        pdf.set_font("Arial", "B", 12)
        pdf.cell(col_id, 10, "ID", border=1)
        pdf.cell(col_name, 10, "Name", border=1)
        pdf.cell(col_abilities, 10, "Abilities", border=1, ln=True)

        # Table rows
        pdf.set_font("Arial", size=11)

        for p in data:
            abilities_text = ", ".join(p["abilities"])

            

            # Name cell
            pdf.cell(col_name, 10, p["name"], border=1)

            # Abilities cell (multiline)
            x = pdf.get_x()
            y = pdf.get_y()

            pdf.multi_cell(col_abilities, 10, abilities_text, border=1)

            # Reset cursor for next row
            pdf.set_xy(x + col_abilities, y)

            pdf.ln(10)

        pdf.output(filename)
        print("PDF table saved:", filename)
