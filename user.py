import socket
import time

# Configurações do cliente
host = '192.168.16.149'  # Substitua pelo endereço IP ou nome de host do Computador 2
porta = 12345

# Crie um socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecte-se ao servidor
cliente.connect((host, porta))

# Função que envia um arquivo para o servidor
def enviar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'rb') as arquivo:
        while True:
            dados = arquivo.read(1024)
            if not dados:
                break
            cliente.send(dados)

    print(f"Arquivo '{nome_arquivo}' enviado com sucesso")

# Nome do arquivo a ser enviado
nome_arquivo = 'teste.txt'  # Substitua pelo nome do seu arquivo

# Enviar o arquivo para o servidor
enviar_arquivo(nome_arquivo)

# Feche a conexão com o servidor
cliente.close()