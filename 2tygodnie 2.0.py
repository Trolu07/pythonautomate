import pandas as pd

# Wczytaj dane z arkusza Excela
df = pd.read_excel('twoj_plik.xlsx')

# Przekształć format daty w kolumnie 'Zaktualizowano' na amerykański
df['Zaktualizowano'] = pd.to_datetime(df['Zaktualizowano'], format='%d, %B %Y %H:%M')

# Oblicz dwutygodniową różnicę dat
from datetime import datetime, timedelta
current_date = datetime.now()
two_weeks_ago = current_date - timedelta(weeks=2)

# Wyfiltruj dane na podstawie daty
df_filtered = df[df['Zaktualizowano'] >= two_weeks_ago]

# Przywróć oryginalny format daty
df_filtered['Zaktualizowano'] = df_filtered['Zaktualizowano'].dt.strftime('%d, %B %Y %H:%M')

# Zapisz wynik przetwarzania do nowego arkusza Excela
df_filtered.to_excel('nowy_plik.xlsx', index=False)
