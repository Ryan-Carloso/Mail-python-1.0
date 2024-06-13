pq n ta. funcionando?

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

# Obtém a data atual
data_atual = datetime.now()

# Adiciona 2 dias à data atual
nova_data = data_atual + timedelta(days=2)

# Formata a nova data no formato MM/DD/YYYY
data_formatada = nova_data.strftime('%m/%d/%Y')

# Função para enviar email
def enviar_email(email, remente):
    time.sleep(1)  # Dê tempo suficiente para alternar entre as janelas
    pyautogui.hotkey('command')  # Alternar para a próxima janela (no macOS)
    # Abrir o navegador Chrome usando PyAutoGUI
    time.sleep(20)
    # Esperar que o Google Chrome seja aberto
    pyautogui.hotkey('command', 't')  # Seleciona a barra de endereço no macOS
    time.sleep(3)
    
    

    # Mova o cursor para a barra de endereço e clique para entrar na URL do Gmail
    pyautogui.click(x=100, y=100)  # Mude as coordenadas de acordo com a sua tela
    gmail_url = f'https://mail.google.com/mail/u/0/?authuser={remente}&view=cm&to={email}&su=%5BBinance%5D%20Request%20to%20Reset%20Security%20Items%20From%2084.193.82.102'
    pyautogui.write(gmail_url)
    print(gmail_url)
    pyautogui.press('enter')
    time.sleep(15)
    
    # click html 
    
    pyautogui.click(438,767)
    time.sleep(5)
    
    # click aplicar into html 
        
    pyautogui.click(1174,731)
    time.sleep(5)
    
    #click schedule  send
    
    pyautogui.click(145, 765)
    time.sleep(4)
    
    
    #click schedule  send  2.
    
    pyautogui.click(144, 731)
    time.sleep(4)    
    #click choose date and time
    
    pyautogui.click(595, 561)
    time.sleep(4)    
        
    pyautogui.click(809, 364)
    time.sleep(4)    
    #delete date
    
    for _ in range(20):
        pyautogui.hotkey('backspace')
        # Aguarda um pequeno intervalo entre cada pressionamento
        time.sleep(0.01)  # Ajuste este valor conforme necessáriopyautogui.hotkey('backspace')    

            
                    #month / day / year
    pyautogui.write(data_formatada)
    time.sleep(5)
    
    
    pyautogui.click(790,417)
    time.sleep(3)
    
    for _ in range(10):
        pyautogui.hotkey('backspace')
        # Aguarda um pequeno intervalo entre cada pressionamento
        time.sleep(0.01)  # Ajuste este valor conforme necessáriopyautogui.hotkey('backspace')    
        
    pyautogui.write(hora_formatada)
    
    time.sleep(4)
         
    pyautogui.click(808, 633)
    time.sleep(3)         
    
    
    pyautogui.hotkey('command', 'w')  # Seleciona a barra de endereço no macOS
    
    

    



    
    
    # Aqui você pode adicionar mais comandos para preencher o corpo do email e enviar
    # ...

# Loop para enviar emails a partir de todas as combinações de remetentes e destinatários
while True:
    # Loop através de todos os emails e remetentes
    for email in email_list.emails:
        for remente in remente_list.rementes:
            enviar_email(email, remente)
            time.sleep(10)  # Aguardar um pouco entre os envios para evitar problemas de sobrecarga
    
    # Aguardar a entrada para continuar ou parar
    input("Pressione Enter para continuar ou Enter novamente para parar.")
    if input() == "":
        break  # Sai do loop quando Enter é pressionado novamente
