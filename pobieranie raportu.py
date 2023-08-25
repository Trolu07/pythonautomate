from selenium import webdriver
import requests
import shutil
import os

# Ścieżka do sterownika przeglądarki, np. chromedriver.exe
driver_path = 'ścieżka/do/sterownika/chromedriver.exe'

# Ścieżka do folderu docelowego, gdzie ma być przeniesiony plik
docelowy_folder = 'ścieżka/do/folderu/docelowego'

# Tworzenie obiektu przeglądarki
driver = webdriver.Chrome(executable_path=driver_path)

# Otwarcie nowej karty i przejście do linku
link = 'adres_linku_do_pobrania_pliku'
driver.execute_script("window.open('', '_blank');")
driver.switch_to.window(driver.window_handles[-1])
driver.get(link)

# Pobranie pliku
response = requests.get(link, stream=True)
plik_do_pobrania = 'nazwa_pliku_do_pobrania.pdf'  # Nazwa pliku do pobrania
with open(plik_do_pobrania, 'wb') as f:
    shutil.copyfileobj(response.raw, f)

# Zamknięcie przeglądarki
driver.quit()

# Przeniesienie pliku do folderu docelowego
sciezka_pliku = os.path.abspath(plik_do_pobrania)
sciezka_docelowa = os.path.join(docelowy_folder, plik_do_pobrania)
shutil.move(sciezka_pliku, sciezka_docelowa)
