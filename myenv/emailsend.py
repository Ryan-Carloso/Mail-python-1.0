import time
import pyautogui
from datetime import datetime, timedelta
import random
import email_list
import remente_list

# Função para gerar uma hora aleatória entre 08:00 e 18:00
def hora_aleatoria():
    hora = random.randint(8, 17)  # Gera uma hora entre 08 e 17
    minuto = random.randint(0, 59)  # Gera um minuto entre 00 e 59
    return f'{hora:02}:{minuto:02}'  # Formata a hora e minuto como HH:MM

# Função para enviar email
def enviar_email(email, remente):
    # Obtém a data atual e adiciona 2 dias
    data_atual = datetime.now()
    nova_data = data_atual + timedelta(days=2)
    data_formatada = nova_data.strftime('%m/%d/%Y')

    # Gera uma hora aleatória
    hora_formatada = hora_aleatoria()

    # Tempo para alternar entre janelas e abrir o navegador
    time.sleep(1)
    pyautogui.hotkey('command', 'tab')  # Alternar para a próxima janela (no macOS)
    time.sleep(20)  # Esperar que o Google Chrome seja aberto

    # Abre uma nova aba no navegador
    pyautogui.hotkey('command', 't')  # Abre uma nova aba (no macOS)
    time.sleep(3)

    # Mova o cursor para a barra de endereço e clique para entrar na URL do Gmail
    pyautogui.click(x=100, y=100)  # Ajuste as coordenadas conforme necessário
    gmail_url = f'https://mail.google.com/mail/u/0/?authuser={remente}&view=cm&to={email}&su=%5BBinance%5D%20Request%20to%20Reset%20Security%20Items%20From%2084.193.82.102'
    pyautogui.write(gmail_url)
    print(gmail_url)
    pyautogui.press('enter')
    time.sleep(15)

    # Interagir com a interface do Gmail
    pyautogui.click(438, 767)
    time.sleep(5)
    pyautogui.click(1174, 731)
    time.sleep(5)
    pyautogui.click(145, 765)
    time.sleep(4)
    pyautogui.click(144, 731)
    time.sleep(4)
    pyautogui.click(595, 561)
    time.sleep(4)
    pyautogui.click(809, 364)
    time.sleep(4)

    # Deletar a data antiga
    for _ in range(20):
        pyautogui.hotkey('backspace')
        time.sleep(0.01)

    # Escrever a nova data
    pyautogui.write(data_formatada)
    time.sleep(5)
    pyautogui.click(790, 417)
    time.sleep(3)

    # Deletar a hora antiga
    for _ in range(10):
        pyautogui.hotkey('backspace')
        time.sleep(0.01)

    # Escrever a nova hora
    pyautogui.write(hora_formatada)
    time.sleep(4)

    # Confirmar o agendamento do envio
    pyautogui.click(808, 633)
    time.sleep(3)

    # Fechar a aba do navegador
    pyautogui.hotkey('command', 'w')

# Loop para enviar emails a partir de todas as combinações de remetentes e destinatários
while True:
    for email in email_list.emails:
        for remente in remente_list.rementes:
            enviar_email(email, remente)
            time.sleep(10)  # Aguardar um pouco entre os envios para evitar problemas de sobrecarga
    
    # Aguardar a entrada para continuar ou parar
    if input("Pressione Enter para continuar ou Enter novamente para parar: ") == "":
        break  # Sai do loop quando Enter é pressionado novamente
