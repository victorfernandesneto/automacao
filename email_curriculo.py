import pyautogui
import pyperclip
import os
from dotenv import load_dotenv


# Função para evitar repetição de código.
def copia_cola(mensagem):
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl', 'v')


def pressiona_enter():
    pyautogui.press('enter')


def envia_curriculo():

    # Solicitando para o usuário os valores para enviar no email.
    seu_nome = input('Qual o seu nome?')
    seu_email = input('Qual seu email?')
    seu_telefone = input('Qual seu telefone para contato?')
    nome_da_vaga = input('Digite o nome da vaga:')
    caminho_curriculo = input('Onde está o currículo no seu computador?')


    # Corpo do email criado a partir das variáveis dadas pelo usuário.
    corpo_do_email = f'''Prezados,
    
    Espero que esta mensagem encontre você bem. Gostaria de expressar meu interesse na posição de {nome_da_vaga}.
    
    Anexo a este e-mail, você encontrará o meu currículo, que fornece mais informações sobre a minha formação acadêmica e histórico de trabalho.
    
    Estou muito animado com a oportunidade de fazer parte do corpo docente e contribuir para o sucesso da equipe. Gostaria de discutir mais sobre como minhas habilidades e experiência podem beneficiar sua organização. Por favor, sinta-se à vontade para entrar em contato comigo por e-mail ({seu_email}) ou por telefone ({seu_telefone}) para agendar uma conversa.
    
    Agradeço pela atenção.
    
    Atenciosamente,
    {seu_nome}
    {seu_telefone}
    {seu_email}'''


    # Os emails para envio na .env devem estar separados somente por vírgulas.
    # Exemplo: LISTA_DE_EMAILS = email1@email.com,email2@gmail.com,email3@gmail.com
    load_dotenv()
    lista_de_emails = os.getenv('LISTA_DE_EMAILS')
    lista_de_emails = lista_de_emails.split(',')  # Transformando a string em uma lista.


    # Abrindo o Chrome e o gmail.
    pyautogui.press('win')
    pyautogui.typewrite('chrome')
    pressiona_enter()
    pyautogui.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('gmail.com')
    pressiona_enter()
    pyautogui.sleep(2)


    # Para a navegação no gmail funcionar, é necessário ter as shortcuts ligadas.
    pyautogui.press('c')  # Abre um email vazio.
    pyautogui.sleep(1)
    copia_cola(seu_email)
    pyautogui.hotkey('ctrl', 'shift', 'b')  # Navega para a aba de Bcc.
    for email in lista_de_emails:
        copia_cola(email)
        pyautogui.sleep(.1)
    pyautogui.press('tab')
    copia_cola(f'Currículo para vaga de {nome_da_vaga}')
    pyautogui.press('tab')
    copia_cola(corpo_do_email)
    pyautogui.sleep(.5)
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')
    pyautogui.sleep(.5)
    copia_cola(caminho_curriculo)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'enter')


if (__name__ == '__main__'):
    envia_curriculo()
