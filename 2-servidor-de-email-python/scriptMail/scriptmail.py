import os
import smtplib
from email.message import EmailMessage
from senhaCrypto import senha

#Configura email senha
EMAIL_ADRESS = 'diego.ab.eletricista@gmail.com'
EMAIL_PASSWORD = senha

#Criar um email
msg = EmailMessage()
msg['From'] = 'email do remetende'
msg['To'] = 'email de quem vai receber a mensagem'
msg['Subject'] = 'Assunto do email'

msg.set_content(' texto que será enviado ')

#enviar email
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print('Seu email foi enviado com sucesso')

'''
Foi criado em dois scripts para a devolução de exercício
pode ser feito apenas com 1 mantendo a senha do email exposta
Ainda faltam os tratamentos de erro
'''