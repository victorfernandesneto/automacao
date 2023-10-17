# Programa que captura e imprime os valores do dólar e do euro no momento atual.
# Se o computador for lento, use pyautogui.sleep(segundos) em alguns trechos do código para esperar o computador processar.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

# Abre o Chrome na página do Google.
chrome = webdriver.Chrome()
chrome.get('https://google.com/')

# Coleta e imprime o valor do dólar.
chrome.find_element(By.ID, 'APjFqb').send_keys('Dólar hoje')
chrome.find_element(By.ID, 'APjFqb').send_keys(Keys.RETURN) # Alternativa: pyautogui.press('enter')
xpath_dolar = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
dolar_hoje_google = chrome.find_element(By.XPATH, xpath_dolar).text
print(f'Dólar hoje = {dolar_hoje_google} reais')

# Coleta e imprime o valor do euro.
chrome.find_element(By.ID, 'APjFqb').send_keys('')
pyautogui.hotkey('tab', 'enter')
chrome.find_element(By.ID, 'APjFqb').send_keys('Euro hoje')
chrome.find_element(By.ID, 'APjFqb').send_keys(Keys.RETURN)
xpath_euro = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
euro_hoje_google = chrome.find_element(By.XPATH, xpath_euro).text
print(f'Euro hoje = {euro_hoje_google} reais')
chrome.close()