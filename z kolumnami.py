import os
import pandas as pd

# Ścieżka do folderu z plikami Excel
folder_path = r'C:\Users\sebas\OneDrive\Pulpit\Project excel\SONY'

# Lista nazw wybranych kolumn
selected_columns = ['kolumna1', 'kolumna2']  # Dodaj tutaj nazwy kolumn, które chcesz zachować

# Inicjalizacja DataFrame, do którego będą dodawane dane
merged_df = pd.DataFrame()

# Przetwarzanie każdego pliku w folderze
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path)
        selected_data = df[selected_columns]
        merged_df = pd.concat([merged_df, selected_data], ignore_index=True)

# Ścieżka do pliku wyjściowego
output_file = os.path.join(folder_path, 'zestawienie.xlsx')

# Zapis do pliku wyjściowego
merged_df.to_excel(output_file, index=False)
print("Zestawienie zostało zapisane do pliku:", output_file)
