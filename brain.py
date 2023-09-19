import RecoFala
import ArvoreDeDecisao as chooses

FalaOuTexto = input("Coloque:\nT = texto\nF = Fala\n")

if str(FalaOuTexto).upper() == "T":
    prompt = input("Faça uma pergunta: ")
    chooses.decisoes.choose(prompt)
else:
    RecoFala.voiceRecord(True)
                
# ------------------------------Informações Legais------------------------------
# Projeto iniciado a aproximadamente 1 semana, hoje é dia 15 de agosto de 2023
# Total de horas estará errado pois comeceu a contar ontem a noite, porém é legal pra ter uma idéia
# Total de horas gastas no projeto: 30hr30min