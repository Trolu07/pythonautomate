import os
import shutil
import pandas as pd

# Ścieżki do folderów
folder_zrodlowy = 'ścieżka_do_folderu_z_pierwszymi_plikami'
folder_docelowy = 'ścieżka_do_folderu_z_przekształconymi_plikami'

# Przeniesienie pliku .csv
lista_plikow = os.listdir(folder_zrodlowy)
if lista_plikow:
    ostatni_plik = max(lista_plikow, key=os.path.getctime)
    sciezka_zrodlowa = os.path.join(folder_zrodlowy, ostatni_plik)
    sciezka_docelowa = os.path.join(folder_docelowy, ostatni_plik)
    
    shutil.move(sciezka_zrodlowa, sciezka_docelowa)
    print(f'Przeniesiono plik {ostatni_plik} do folderu docelowego.')

# Konwersja pliku .csv na .xlsx
if os.path.exists(sciezka_docelowa):
    nazwa_pliku_bez_rozszerzenia = os.path.splitext(ostatni_plik)[0]
    sciezka_pliku_xlsx = os.path.join(folder_docelowy, f'{nazwa_pliku_bez_rozszerzenia}.xlsx')
    
    df = pd.read_csv(sciezka_docelowa)  # Wczytanie pliku .csv do DataFrame
    df.to_excel(sciezka_pliku_xlsx, index=False)  # Zapisanie DataFrame jako plik .xlsx
    
    print(f'Konwertowano plik {ostatni_plik} na format .xlsx.')
