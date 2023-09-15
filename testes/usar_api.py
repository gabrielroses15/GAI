import api as chatbot

x = 0

while x<5:
    x = x+1
    frase = input("Escreva:\n")
    chatbot.decisoes.choose(frase)