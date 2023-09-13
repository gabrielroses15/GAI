import spacy
from googletrans import Translator
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

nlp = spacy.load("en_core_web_sm")

#Função pra traduzir um prompt
def trad(text):
    translator = Translator()
    translated_text = translator.translate(text, src='auto', dest='en').text
    return translated_text

#VerificaSaudação
def is_saudacao(prompt):
    doc = nlp(prompt.lower())
    
    saudacoes = ["hi", "hello", "hey"]
    
    for token in doc:
        if token.text in saudacoes:
            return True
    
    return False

# Início da árvore de Decisão:

def choose(prompt=str):
    #Criando uma lista de tipos, buscando otimização no entendimento do contexto.
    #Considero que seja melhor dar um append do que verificar tipo a tipo.
    tipos = []

    #Dicionário de palavras
    key_saudacoes =  ["oiee","oie","oii","oi","eae","olá","ola","salve","e ai","e aí","saudações", 
                   "saudaçoes", "saudacões", "saudacoes", "saudacao", "saudacão"]
    
    key_question = ["quem", "como", "quando", "pq", "onde", "qual"]

    key_thx = ["obrigado", "valeu", "obrigada", "vlw"]

    dicio = [key_saudacoes, key_question, key_thx]
    
    #Início padrão
    start = "considerando sua frase, "
    saudacao = "Olá, "

    #Verificações baseadas no dicionário
    for lista in dicio:
        if any(item in prompt.lower() for item in lista):
            if lista == key_saudacoes:
                tipos.append("saudacao")
                saudacao = next((item for item in lista if item in prompt.lower()), None)
            elif lista == key_question:
                tipos.append("question")
                start = "Considerando sua pergunta, "
            elif lista == key_thx:
                tipos.append("thx")
                #Ele deverá escolher entre as variantes, pois pode ser apenas "obrigado"
                #Ou ser "obrigado, mas gostaria de saber..."
                # start = "De nada"
                # start = "De nada, "
                #Deve-se  considerar também frases como "bom dia, obrigado por..." ondne há mais de um start
                #Necessário para "suprir" a frase.
    
    #Verifica dia/tarde/noite

    if "bom dia" in prompt.lower():
        tipos.append("dia")
        start = "Bom dia, "

    if "boa tarde" in prompt.lower():
        tipos.append("tarde")
        start = "Boa tarde, "

    if "boa noite" in prompt.lower():
        tipos.append("noite")
        start = "Boa noite, "

    
    #Construção do "start"

    if saudacao == "Olá, ":
        start = saudacao + start
    else:
        if "thx" in tipos:
            start = saudacao + "É um prazer te ajudar, " + start
        start = saudacao + start



    print("tipo = {} e start = {}".format(tipos, start))

x = 0

while x<5:
    x = x+1
    frase = input("Escreva:\n")
    choose(frase)