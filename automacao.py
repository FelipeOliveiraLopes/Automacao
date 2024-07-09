import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = 'your_email@example.com'
    from_password = 'your_password'
    
    # Configurações do servidor SMTP
    smtp_server = 'smtp.example.com'
    smtp_port = 587

    # Criação do objeto de mensagem
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Adicionando o corpo do email
    msg.attach(MIMEText(body, 'plain'))

    # Enviando o email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print('Email enviado com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Exemplo de uso
send_email('Assunto do Email', 'Corpo do email', 'destinatario@example.com')