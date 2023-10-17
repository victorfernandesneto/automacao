# Programa que captura e imprime os valores do dólar e do euro no momento atual.
# Se o computador for lento, use pyautogui.sleep(segundos) em alguns trechos do código para esperar o computador processar.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import xlsxwriter
import os


# Abre o Chrome na página do Google.
chrome = webdriver.Chrome()
chrome.get('https://google.com/')

# Coleta o valor do dólar.
chrome.find_element(By.ID, 'APjFqb').send_keys('Dólar hoje')
chrome.find_element(By.ID, 'APjFqb').send_keys(Keys.RETURN)
# Alternativa: pyautogui.press('enter')
xpath_dolar = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'

dolar_hoje_google = chrome.find_element(By.XPATH, xpath_dolar).text

# Replace necessário para poder transformar o valor em float.
dolar_hoje_google = dolar_hoje_google.replace(",", ".")
dolar_hoje_google = float(dolar_hoje_google)

# Coleta o valor do euro.
chrome.find_element(By.ID, 'APjFqb').send_keys('')
pyautogui.hotkey('tab', 'enter')
chrome.find_element(By.ID, 'APjFqb').send_keys('Euro hoje')
chrome.find_element(By.ID, 'APjFqb').send_keys(Keys.RETURN)
# Alternativa: pyautogui.press('enter')
xpath_euro = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'

euro_hoje_google = chrome.find_element(By.XPATH, xpath_euro).text
# Replace necessário para poder transformar o valor em float.
euro_hoje_google = euro_hoje_google.replace(",", ".")
euro_hoje_google = float(euro_hoje_google)

chrome.close()

# Imprime os valores.
print(f'Dólar hoje = {dolar_hoje_google} reais')
print(f'Euro hoje = {euro_hoje_google} reais')

# # Se quiser imprimir os valores em uma planilha Excel, descomente o código abaixo.
# caminho_arquivo = r"C:\planilhas\Dolar e Euro Google.xlsx"
# planilha_criada = xlsxwriter.Workbook(caminho_arquivo)
# planilha1 = planilha_criada.add_worksheet()
#
# planilha1.write("A1", "Dólar")
# planilha1.write("B1", "Euro")
# planilha1.write("A2", dolar_hoje_google)
# planilha1.write("B2", euro_hoje_google)
#
# planilha_criada.close()
#
# # Abrir o arquivo pronto.
# os.startfile(caminho_arquivo)