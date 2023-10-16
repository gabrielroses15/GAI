import socket

# Configurações do cliente
host = '127.0.0.1'  # Substitua pelo endereço IP ou nome de host do Computador 2
porta = 12345

# Crie um socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecte-se ao servidor
cliente.connect((host, porta))

# Função que faz uma solicitação ao servidor
def solicitar_execucao_codigo(codigo):
    cliente.send(codigo.encode('utf-8'))
    print("Solicitação enviada para o Computador 2")
    
    resposta = cliente.recv(1024).decode('utf-8')
    
    print("Resposta do Computador 2:")
    print(resposta)
    
    # Feche a conexão após receber a resposta
    cliente.close()

# Código Python que você deseja executar no Computador 2
codigo_a_executar = """
pip install transformers
"""

# Solicite a execução do código
solicitar_execucao_codigo(codigo_a_executar)
