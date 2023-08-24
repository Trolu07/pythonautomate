import os
import pandas as pd
from openpyxl import Workbook

source_folder = r'C:\Users\sebas\OneDrive\Pulpit\Project excel\SONY'
output_file = r'C:\Users\sebas\OneDrive\Pulpit\Project excel\Raport.xlsx'

# Puste DataFrame do przechowywania zestawienia
merged_data = pd.DataFrame()

# Przechodzimy przez pliki w folderze
for filename in os.listdir(source_folder):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(source_folder, filename)
        df = pd.read_excel(file_path, usecols=['lp', 'lok'])  # Wybierz interesujące kolumny
        merged_data = pd.concat([merged_data, df], ignore_index=True)

# Tworzymy nowy arkusz Excel do zapisania zestawienia
workbook = Workbook()
sheet = workbook.active

# Zapisujemy dane z DataFrame do arkusza
for row in pd.DataFrame.iterrows(merged_data):
    sheet.append(row[1].tolist())

# Zapisujemy arkusz jako plik Excel
workbook.save(output_file)

print("Zestawienie zostało zapisane do pliku:", output_file)
