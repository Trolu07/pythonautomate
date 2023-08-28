import os
import pandas as pd

# Ścieżki do folderów
folder_zrodlowy = 'ścieżka_do_folderu_A'
folder_docelowy = 'ścieżka_do_folderu_B'

# Przerobienie plików CSV na XLSX i przeniesienie do folderu docelowego
lista_plikow = os.listdir(folder_zrodlowy)
for plik in lista_plikow:
    if plik.lower().endswith('.csv'):
        sciezka_pliku_csv = os.path.join(folder_zrodlowy, plik)
        nazwa_pliku_bez_rozszerzenia = os.path.splitext(plik)[0]
        sciezka_pliku_xlsx = os.path.join(folder_docelowy, f'{nazwa_pliku_bez_rozszerzenia}.xlsx')
        
        df = pd.read_csv(sciezka_pliku_csv)  # Wczytanie pliku CSV do DataFrame
        df.to_excel(sciezka_pliku_xlsx, index=False)  # Zapisanie DataFrame jako plik XLSX
        
        print(f'Przerobiono plik {plik} na format XLSX i zapisano do folderu docelowego.')

# Usunięcie plików CSV z folderu źródłowego
for plik in lista_plikow:
    if plik.lower().endswith('.csv'):
        sciezka_pliku_csv = os.path.join(folder_zrodlowy, plik)
        os.remove(sciezka_pliku_csv)
        print(f'Usunięto plik {plik} z folderu źródłowego.')
