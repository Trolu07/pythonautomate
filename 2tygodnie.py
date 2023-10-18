import pandas as pd
from datetime import datetime, timedelta

# Wczytaj dane z arkusza Excela
df = pd.read_excel('twoj_plik.xlsx')

# Ustal datę, od której chcesz zachować wiersze (np. ostatnie 2 tygodnie)
data_początkowa = datetime.now() - timedelta(weeks=2)

# Wykonaj filtrowanie na podstawie daty w kolumnie 'data'
df['data'] = pd.to_datetime(df['data'])  # Upewnij się, że 'data' to kolumna z datą
df_filtr = df[df['data'] >= data_początkowa]

# Zapisz wynik filtrowania do nowego arkusza Excela
df_filtr.to_excel('nowy_plik.xlsx', index=False)
