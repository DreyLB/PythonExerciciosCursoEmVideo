from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.climatempo.com.br/")

time.sleep(5)

tempo = driver.find_element(By.ID, "current-weather-temperature")

print(f"Hoje o tempo é de {tempo.text} graus")