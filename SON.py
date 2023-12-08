import os
import pandas as pd

# Ścieżki do folderu wejściowego (A) i folderu wyjściowego (B)
folder_A = "ścieżka_do_folderu_A"
folder_B = "ścieżka_do_folderu_B"

# Utwórz listę plików .xlsx w folderze A
pliki_xlsx = [plik for plik in os.listdir(folder_A) if plik.endswith(".xlsx")]

# Utwórz pustą ramkę danych do przechowywania zbiorczego zestawienia
zbiorcze_zestawienie = pd.DataFrame(columns=["Nazwa Pliku", "A", "B", "C", "D", "E", "F", "G", "H"])

# Iteruj przez pliki .xlsx
for plik in pliki_xlsx:
    # Odczytaj dane z pliku .xlsx
    ścieżka_pliku = os.path.join(folder_A, plik)
    df = pd.read_excel(ścieżka_pliku)

    # Pobierz odpowiednie komórki i dodaj do zbiorczego zestawienia
    wiersz = [plik, df.at[2, "B"], df.at[3, "B"], df.at[4, "B"], df.at[6, "B"], df.at[7, "B"], df.at[14, "B"], df.at[38, "D"]]
    zbiorcze_zestawienie = zbiorcze_zestawienie.append(pd.Series(wiersz, index=zbiorcze_zestawienie.columns), ignore_index=True)

# Zapisz zbiorcze zestawienie do nowego pliku .xlsx w folderze B
ścieżka_wyjściowa = os.path.join(folder_B, "zbiorcze_zestawienie.xlsx")
zbiorcze_zestawienie.to_excel(ścieżka_wyjściowa, index=False)
