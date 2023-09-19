import numpy as np
import tkinter as tk
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import CalculaSentimento
import socket
import threading
import os

# Função para receber e salvar o arquivo
def receber_arquivo(cliente, nome_arquivo):
    with open(nome_arquivo, 'wb') as arquivo:
        while True:
            dados = cliente.recv(1024)
            if not dados:
                break
            arquivo.write(dados)
    
    print(f"Arquivo '{nome_arquivo}' recebido com sucesso")

def handle_client(cliente, endereco):
    print(f"Conexão recebida de {endereco}")

    # Nome do arquivo a ser recebido (você pode escolher o nome no servidor)
    nome_arquivo = 'arquivo_recebido.txt'

    # Receber o arquivo e salvá-lo localmente
    receber_arquivo(cliente, nome_arquivo)

    # Fecha a conexão com o cliente
    cliente.close()

    # Função para carregar dados de um arquivo JSON
    def carregar_dados(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        data = []
        sentimentos = []
        last_mensageiro = None
        msg = ""

        for linha in linhas:
            if "<arquivo de mídia oculto>" in linha.lower():
                continue
            if "Mensagem apagada" in linha:
                continue
            if "chamada de voz perdida" in linha:
                continue
            elif " - " in linha:
                linha = linha.lower()
                linha = linha.split(" - ")
                linha = linha[1]
                linha = linha.replace("\n", "")

                mensageiro = linha.split(":")[0]

                linha = linha.replace(mensageiro, "")
                mensagem = linha.replace(":", "")

                if mensageiro == last_mensageiro:
                    msg += mensagem 
                else:
                    if last_mensageiro is not None:
                        data.append((last_mensageiro, msg))
                        sentimentos.append(CalculaSentimento.CalcFeeling(msg, False))
                    msg = mensagem
                    last_mensageiro = mensageiro
            else:
                continue

        if last_mensageiro is not None:
            data.append((last_mensageiro, msg))
            sentimentos.append(CalculaSentimento.CalcFeeling(msg, False))

        mensagens, rotulos = zip(*data)
        return mensagens, rotulos, sentimentos

    # Função para salvar dados em um arquivo JSON
    def salvar_dados(nome_arquivo, mensagens, rotulos, sentimentos):
        with open(nome_arquivo, 'a', encoding='utf-8') as f:
            for mensagem, remetente, sentimento in zip(mensagens, rotulos, sentimentos):
                f.write(f"{remetente} - {mensagem} - {sentimento}\n")

    # Carregar os dados do arquivo recebido
    mensagens, rotulos, sentimentos = carregar_dados(nome_arquivo)
    data = list(zip(rotulos, mensagens))

    # Salvar os dados em um arquivo (modo de adição)
    salvar_dados("dados_combinados.txt", [item[1] for item in data], [item[0] for item in data], sentimentos)

    # Vetorização de texto usando bag of words (BoW)
    vectorizer = CountVectorizer()

    # Lematização usando spaCy
    def lematizar_texto(texto):
        tokens = nlp(texto)
        lemas = [token.lemma_ for token in tokens]
        return " ".join(lemas)

    X = vectorizer.fit_transform([f"{lematizar_texto(item[1])} {sentimento}" for item, sentimento in zip(data, sentimentos)])

    # Treinamento do classificador (Neste exemplo, usamos o Naive Bayes)
    classifier = MultinomialNB()
    classifier.fit(X, [item[0] for item in data])

    while True:
        
        mensagem_pronta = "Pronto para mais TXT\n"
        
        cliente.send(mensagem_pronta.encode())
        
        nova_mensagem = input("Escreva algo (ou 'sair' para encerrar): ").lower()

        if nova_mensagem.lower() == 'sair':
            break

        # Lematização da nova mensagem
        nova_mensagem_lematizada = lematizar_texto(nova_mensagem)

        nova_mensagem_transformed = vectorizer.transform([nova_mensagem_lematizada])

        # Obtendo as probabilidades das classes (remetentes)
        probabilidades = classifier.predict_proba(nova_mensagem_transformed)[0]

        # Defina a temperatura para controlar a aleatoriedade (valores mais altos tornam as respostas mais aleatórias)
        temperatura = 0.5

        # Aplicar a "temperatura" às probabilidades para tornar as respostas mais ou menos aleatórias
        probabilidades_ajustadas = np.exp(np.log(probabilidades) / temperatura)
        probabilidades_ajustadas /= probabilidades_ajustadas.sum()

        # Escolher aleatoriamente uma resposta com base nas probabilidades ajustadas
        resposta_aleatoria = np.random.choice(classifier.classes_, p=probabilidades_ajustadas)
        print(f'Remetente previsto para a nova mensagem: {resposta_aleatoria}')

# Configurações do servidor
host = '0.0.0.0'  # Use '0.0.0.0' para aceitar conexões de qualquer IP
porta = 65535

# Crie um socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincule o socket ao endereço e porta
servidor.bind((host, porta))

# Espere por conexões em fila
servidor.listen()

print(f"Servidor esperando por conexões em {host}:{porta}")

nlp = spacy.load("en_core_web_sm")

# Mantenha o servidor em execução indefinidamente
while True:
    try:
        cliente, endereco = servidor.accept()
        cliente_thread = threading.Thread(target=handle_client, args=(cliente, endereco))
        cliente_thread.start()
    except KeyboardInterrupt:
        print("Servidor encerrado.")
        break
