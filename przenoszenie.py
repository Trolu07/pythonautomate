from selenium import webdriver
import os
import shutil

# Ustal ścieżki do plików
download_directory = r'C:\ścieżka\do\folderu\pobierania'
destination_directory = r'C:\ścieżka\do\innego\folderu'

# Otwórz przeglądarkę
driver = webdriver.Chrome()

# Otwórz link
driver.get('twój_link_do_pobrania')

# Pobierz plik
# tutaj kod do pobierania pliku

# Zamknij przeglądarkę
driver.quit()

# Pobierz nazwę ostatnio pobranego pliku
last_downloaded_file = max([os.path.join(download_directory, f) for f in os.listdir(download_directory)], key=os.path.getctime)

# Przenieś plik do innego folderu
shutil.move(last_downloaded_file, os.path.join(destination_directory, os.path.basename(last_downloaded_file)))

print("Plik został przeniesiony.")
