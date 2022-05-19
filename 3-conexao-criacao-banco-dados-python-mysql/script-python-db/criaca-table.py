import mysql.connector

#Criar conexão com banco de dados
c = mysql.connector.connect(
    host='localhost',
    user='root',
    database='KONOHA',
    password='Mudeidevida20$')
cursor = c.cursor()


createTable = '''CREATE TABLE STUDENTS_NINJAS (name VARCHAR(30),
                age INT(3),
                sex CHAR(1),
                cla VARCHAR(15),
                main_jutsu VARCHAR(15),
                best_jutsu VARCHAR(15))
               ''' 
cursor.execute(createTable)

cursor.execute('DESCRIBE students')
dados = cursor.fetchall()
print('Resultado da busca em KONOHA ->>', dados)
if c.is_connected():
    cursor.close()
    c.close()
print('Conexão encerrada')
