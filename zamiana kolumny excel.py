import pandas as pd

# Wczytaj plik Excel
df = pd.read_excel('nazwa_pliku.xlsx')

# Zdefiniuj funkcję, która pozostawi tylko 10 pierwszych znaków
def obetnij_do_10_znakow(text):
    return text[:10]

# Zastosuj funkcję do danej kolumny
df['nazwa_kolumny'] = df['nazwa_kolumny'].apply(obetnij_do_10_znakow)

# Zapisz zmienione dane z powrotem do pliku Excel
df.to_excel('nazwa_pliku_zmieniony.xlsx', index=False)
