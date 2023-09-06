import socket
import threading
import time

# Configurações do servidor
host = '0.0.0.0'  # Use '0.0.0.0' para aceitar conexões de qualquer IP
porta = 12345

# Crie um socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincule o socket ao endereço e porta
servidor.bind((host, porta))

# Espere por até 5 conexões em fila
servidor.listen(5)

print(f"Servidor esperando por conexões em {host}:{porta}")

# Função para executar código Python e enviar o resultado de volta
def executar_codigo(codigo):
    try:
        # Execute o código
        exec(codigo)
        resposta = "Código executado com sucesso."
    except Exception as e:
        resposta = f"Erro: {str(e)}"
    return resposta

# Função que lida com uma conexão de cliente
def lidar_com_cliente(cliente, endereco):
    print(f"Conexão recebida de {endereco}")
    
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            
            if not mensagem:
                break
            
            # Verifique se a mensagem é "fechar" para encerrar a conexão
            if mensagem.strip().lower() == "fechar":
                cliente.send("sair".encode('utf-8'))
                cliente.close()
                break
            
            # Execute o código e obtenha a resposta
            resposta = executar_codigo(mensagem)
            
            # Envie a resposta de volta para o cliente
            cliente.send(resposta.encode('utf-8'))
        
        except ConnectionResetError:
            # Capturar a exceção ConnectionResetError e não fazer nada
            pass

# Loop para aceitar conexões de clientes continuamente
while True:
    cliente, endereco = servidor.accept()
    cliente_thread = threading.Thread(target=lidar_com_cliente, args=(cliente, endereco))
    cliente_thread.start()
