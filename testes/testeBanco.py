import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='gai_register'
)

cursor = conexao.cursor()


comando = f'DELETE FROM usuarios WHERE tokenUsuario = "token"'
cursor.execute(comando)
conexao.commit()

conexao.close()
cursor.close()