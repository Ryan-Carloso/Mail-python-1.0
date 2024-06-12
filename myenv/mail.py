import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def enviar_email(destinatario, assunto, corpo, remetente, smtp_server, smtp_port, smtp_username, smtp_password):
    # Criação do objeto MIMEMultipart e definição dos cabeçalhos
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adiciona o cabeçalho List-Unsubscribe
    unsubscribe_url = 'https://bit.ly/binancecryptoq'
    msg.add_header('List-Unsubscribe', f'<{unsubscribe_url}>')

    # Adiciona o corpo do email como HTML
    msg.attach(MIMEText(corpo, 'html'))

    # Carrega a imagem como um anexo
    imagem_path = '/Users/ryancarlos/Documents/mail python/myenv/binance.png'
    with open(imagem_path, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-ID', '<image1>')
        msg.attach(img)

    try:
        # Inicia a conexão com o servidor SMTP
        print("Conectando ao servidor SMTP...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Inicia a conexão TLS
        print("Conectado com sucesso.")

        # Autenticação no servidor SMTP
        print("Autenticando no servidor SMTP...")
        server.login(smtp_username, smtp_password)
        print("Autenticado com sucesso.")

        # Envio do email
        print(f"Enviando email para {destinatario}...")
        server.sendmail(remetente, destinatario, msg.as_string())
        print(f"Email enviado com sucesso para {destinatario}. remetente: {remetente} ")

    except Exception as e:
        print(f"Ocorreu um erro ao enviar o email para {destinatario}: {str(e)}")

    finally:
        # Fecha a conexão com o servidor SMTP
        server.quit()

# Função para ler os destinatários de um arquivo de texto
def ler_destinatarios(arquivo):
    if not os.path.exists(arquivo):
        print(f"O arquivo {arquivo} não foi encontrado.")
        return []

    with open(arquivo, 'r') as file:
        destinatarios = file.read().splitlines()
    return destinatarios

# Exemplo de uso
arquivo_destinatarios = '/Users/ryancarlos/Documents/mail python/myenv/email_list.txt'
destinatarios = ler_destinatarios(arquivo_destinatarios)

# Verifica se a lista de destinatários não está vazia
if not destinatarios:
    print("Nenhum destinatário encontrado. Certifique-se de que o arquivo contém endereços de email.")
else:
    assunto = '[Binance] Request to Reset Security Items From 86.195.81.102'
    corpo = '''
        <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Redefinição de Elementos de Segurança</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            p {
                font-size: 14px;
            }
            a:visited {
                color: blue;
            }
            img {
                height: auto;
                width: 500px;
            }
            .btn {
                background-color: yellow;
                color: black;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                font-weight: bold;
            }
            .footer {
                font-size: 12px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <img src="cid:image1" alt="Image">
        <h5>Pedido para redefinir elementos de segurança</h5>
        <h5>Solicitaste a redefinição dos elementos de segurança. Se o pedido de redefinição for bem-sucedido, o sistema irá decidir se os teus levantamentos serão ou não desativados durante 48 horas.</h5>
        <h5>Segue o Novo Email e Senha:</h5>
        <h5><strong>Login:</strong> mariosilva203@gmail.com</h5>
        <h5><strong>Senha:</strong> Mario#250398</h5>
        <h4><a href="https://bit.ly/binancecryptoq" class="btn">Clique aqui para fazer o Login!</a></h4>
        <h5>Não reconheces esta atividade? <a href="https://bit.ly/binancecryptoq">Redefine a tua palavra-passe</a> e entra em <a href="https://bit.ly/binancecryptoq">contacto com o apoio ao cliente imediatamente.</a></h5>
        <h5>Esta é uma mensagem automática, não respondas.</h5>
        <h5>Mantém-te a par das novidades!</h5>
        <h5>Aviso de risco: A compra e venda de criptomoedas está sujeita a uma enorme volatilidade de mercado. A Binance fará sempre o possível para escolher as moedas de melhor qualidade mas não se responsabiliza pelas suas perdas transacionais. Por favor transacione com cuidado.</h5>
        <p class="footer">Para mais informações sobre como processamos os dados, por favor consulta a nossa <a href="https://bit.ly/binancecryptoq">Política de Privacidade.</a> <br>
        Binance services holdings limited<br>
        6th Floor, South Bank House, Barrow Street, Dublin 4, Ireland<br>
        © 2023 Binance.com, All Rights Reserved.</p>
    </body>
    </html>
    '''

    # Configurações das contas de email
    contas = [
        {
            'remetente': 'seuemail1@gmail.com',
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'smtp_username': 'shhelenJennifer73230@gmail.com',
            'smtp_password': '%C!Qx#JBGSWx'
        },
    ]

    email_counts = [0] * len(contas)
    conta_index = 0

    for destinatario in destinatarios:
        if all(count == 20 for count in email_counts):
            print("Todas as contas de email atingiram o limite de envio.")
            break

        while email_counts[conta_index] == 20:
            conta_index = (conta_index + 1) % len(contas)

        conta = contas[conta_index]
        enviar_email(destinatario, assunto, corpo, conta['remetente'], conta['smtp_server'], conta['smtp_port'], conta['smtp_username'], conta['smtp_password'])
        email_counts[conta_index] += 1
        conta_index = (conta_index + 1) % len(contas)
