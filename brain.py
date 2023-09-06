import TipoPergunta
import CalculaSentimento
import RecoTheme
import Resposta_Audio
import RecoFala

FalaOuTexto = input("Coloque:\nT = texto\nF = Fala\n")

if str(FalaOuTexto).upper() == "T":
    prompt = input("Faça uma pergunta: ")
    
    strFeel, feel = CalculaSentimento.CalcFeeling(prompt)
    QuestionType = TipoPergunta.QuestionNeuron().QuestionType(prompt)
    theme = RecoTheme.RecoKeys(prompt)
    
    print(strFeel, feel)
    print(QuestionType)
    print("Tema: ", theme)
else:
    RecoFala.voiceRecord(True)
                
# ------------------------------Informações Legais------------------------------
# Projeto iniciado a aproximadamente 1 semana, hoje é dia 26 de agosto de 2023
# Total de horas estará errado pois comeceu a contar ontem a noite, porém é legal pra ter uma idéia
# Total de horas gastas no projeto: 20hr41min