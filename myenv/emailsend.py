import time
import pyautogui
import random
import email_list
import remente_list

# Função para enviar email
def enviar_email(email, remente):
    time.sleep(10)  # Dê tempo suficiente para alternar entre as janelas
    pyautogui.hotkey('command')  # Alternar para a próxima janela (no macOS)
    time.sleep(7)
    pyautogui.hotkey('command', 't')  # Abre uma nova aba no navegador
    time.sleep(6)

    # Mova o cursor para a barra de endereço e clique para entrar na URL do Gmail
    pyautogui.click(x=100, y=100)  # Mude as coordenadas de acordo com a sua tela
    gmail_url = f'https://mail.google.com/mail/u/0/?authuser={remente}&view=cm&to={email}&su=%5BBinance%5D%20Request%20to%20Reset%20Security%20Items%20From%2084.193.82.102'
    pyautogui.write(gmail_url)
    print(f'remente: {remente}  destinario: {email}')  # Correção do print
    pyautogui.press('enter')
    time.sleep(20)
    
    # Click HTML 
    pyautogui.click(438, 767)
    time.sleep(10)
    
    # Click aplicar into HTML 
    pyautogui.click(1174, 731)
    time.sleep(7)
    
    # Click schedule send
    pyautogui.click(145, 765)
    time.sleep(7)
    
    # Click schedule send 2
    pyautogui.click(144, 731)
    time.sleep(7)
    
    # Click in tomorrow afternoon
    num_tabs = random.randint(0, 2)

    # Pressiona a tecla "Tab" um número aleatório de vezes
    for _ in range(num_tabs):
        pyautogui.press('tab')
        time.sleep(0.2)  # Pequena pausa entre as pressões de tecla

    pyautogui.press('enter')

    # Imprime uma mensagem diferente dependendo do valor de num_tabs
    if num_tabs == 0:
        print("Tomorrow morning.")
    elif num_tabs == 1:
        print("Tomorrow Afternoon.")
    elif num_tabs == 2:
        print("Monday or so.")

    time.sleep(6)
    pyautogui.hotkey('command', 'w')  # Fecha a aba atual

# Índices iniciais de remetente e destinatário
index_remetente = 0
index_destinatario = 0

# Loop para enviar emails a partir de todas as combinações de remetentes e destinatários
while True:
    remetente = remente_list.rementes[index_remetente]
    destinatario = email_list.emails[index_destinatario]
    
    enviar_email(destinatario, remetente)
    time.sleep(7)  # Aguardar um pouco entre os envios para evitar problemas de sobrecarga
    
    # Avançar para o próximo remetente e destinatário
    index_remetente += 1
    index_destinatario += 1
    
    # Reiniciar os índices se atingirem o final das listas
    if index_remetente >= len(remente_list.rementes):
        index_remetente = 0
    if index_destinatario >= len(email_list.emails):
        index_destinatario = 0
