#import RecoFala
from DecisionModules import controlador as controller

FalaOuTexto = input("Coloque:\nT = texto\nF = Fala\n")

if str(FalaOuTexto).upper() == "T":
    prompt = input("Faça uma pergunta: ")
    resposta = controller.controller(prompt)#Charles Darwin
#else:
    #RecoFala.voiceRecord(True)
    
#Eu estava andando no museu da praça jose e vi um quadro de napoleao quem foi ele
print(resposta)
                
# ------------------------------Informações Legais------------------------------
# Projeto iniciado a aproximadamente 1 semana, hoje é dia 15 de agosto de 2023
# Total de horas estará errado pois comeceu a contar ontem a noite, porém é legal pra ter uma idéia
# Total de horas gastas no projeto: 51hr00min
# --------------------------------------I---------------------------------------
# Após 49:30min de projeto, GAI finalmente tem divisores por themas realmente funcionais e consegue
# Entender algumas frases que definitivamente não são tão simples como por exemplo "Estava na a
# venida maria e vi as estátuas de davi e salomão, quem foram eles?"
# GAI já entende q se refere a biografia de davi e salomão, mesmo contendo o nome maria em seu banco