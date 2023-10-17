# Programa que preenche formulários na internet com dados de planilhas do Excel.
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from openpyxl import load_workbook

caminho_arquivo = "Lutadores.xlsx"
planilha_lutadores = load_workbook(filename=caminho_arquivo)

planilha_selecionada = planilha_lutadores['Dados']

for i in range(2, len(planilha_selecionada['A']) + 1):  # De 2 porque o A1, B1, ..., são, normalmente, os títulos.
    nome = planilha_selecionada[f'A{i}'].value
    idade = planilha_selecionada[f'B{i}'].value
    peso = float(planilha_selecionada[f'C{i}'].value)

    # Abre o Chrome e o formulário.
    chrome = webdriver.Chrome()
    chrome.get('https://pt.surveymonkey.com/r/5KQQ2B3')
    pyautogui.sleep(.1)  # Para garantir que o computador processou o formulário.

    # Localizando todos os elementos necessários para preencher o formulário.

    # Localização das caixas de nome e idade.
    caixa_nome = chrome.find_element(By.ID, '156982004')
    caixa_idade = chrome.find_element(By.ID, '156982114')

    # Localização do botão dos leves
    botao_leve = chrome.find_element(By.ID, '156982339_1153099265_label')

    # Localização do botão dos médios
    botao_medio = chrome.find_element(By.ID, '156982339_1153099266_label')

    # Localização do botão dos médios
    botao_pesado = chrome.find_element(By.ID, '156982339_1153099267_label')

    # Localização do botão de concluir formulário
    botao_concluido = chrome.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')

    # Enviar as strings
    caixa_nome.send_keys(nome)
    caixa_idade.send_keys(idade)

    # Lógica para apertar o botão de peso (ilustrativo)
    if peso >= 90:
        botao_pesado.click()
    elif peso >= 70:
        botao_medio.click()
    else:
        botao_leve.click()

    # Finalizando o formulário
    botao_concluido.click()
    pyautogui.sleep(.1)
    chrome.close()
