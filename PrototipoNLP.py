import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import CalculaSentimento
import RecoTheme

nlp = spacy.load("en_core_web_sm")

# Função para carregar dados de um arquivo JSON
def carregar_dados(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    data = []
    sentimentos = []
    temas = []  # Adicione esta lista para armazenar os temas

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

            # Chamada para RecoTheme para obter o tema
            tema = RecoTheme.RecoKeys(mensagem, True)
            if tema:
                temas.append(tema)

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
    return mensagens, rotulos, sentimentos, temas

# Função para salvar dados em um arquivo JSON
def salvar_dados(nome_arquivo, mensagens, rotulos, sentimentos, temas):
    with open(nome_arquivo, 'a', encoding='utf-8') as f:
        for mensagem, remetente, sentimento, tema in zip(mensagens, rotulos, sentimentos, temas):
            f.write(f"{remetente} - {mensagem} - {sentimento} - {tema}\n")

# Inicialize os dados como uma lista vazia
data = []

root = tk.Tk()
root.withdraw()  # Fecha a janela principal do tkinter

while True:
    nome_arquivo = filedialog.askopenfilename(title="Escolha um arquivo de dados (ou 'sair' para parar)", filetypes=[("Arquivos de Texto", "*.txt")])
    if not nome_arquivo:
        break

    mensagens, rotulos, sentimentos, temas = carregar_dados(nome_arquivo)
    data.extend(list(zip(rotulos, mensagens)))
    
# Salvar os dados em um arquivo (modo de adição)
salvar_dados("dados_combinados.txt", [item[1] for item in data], [item[0] for item in data], sentimentos, temas)

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
