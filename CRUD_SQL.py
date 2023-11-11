import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dark",
    database="perguntasfeitas"
)

# Delete
#cursor = conexao.cursor()
#id = 2
#comando = f'DELETE from pergunta WHERE idPergunta = {id}'
#cursor.execute(comando)
#conexao.commit()

# Update
#cursor = conexao.cursor()
#pergunta = "pergunta"
#id = 1
#comando = f'UPDATE pergunta SET Pergunta = "{pergunta}" WHERE idPergunta = "{id}"'
#cursor.execute(comando)
#conexao.commit()

# Read
#cursor = conexao.cursor()
#comando = 'SELECT * FROM pergunta'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

# Create
#cursor = conexao.cursor()
#pergunta = "Eae"
#comando = f'INSERT INTO pergunta (pergunta) VALUES ("{pergunta}")'
#cursor.execute(comando)
#conexao.commit()



cursor.close()
conexao.close()
