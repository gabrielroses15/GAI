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
# Total de horas gastas no projeto: 43hr30min