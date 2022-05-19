#criar conexão com mysql
import mysql.connector

#Criar conexão com banco de dados
c = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mudeidevida20$')

#criar banco de dados
cursor = c.cursor()
cursor.execute('CREATE DATABASE KONOHA_VILLAGE')

#fechar conexão
if c.is_connected():
    cursor.close()
    c.close()
print('Conexão encerrada')
