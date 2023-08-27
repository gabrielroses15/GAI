import TipoPergunta
import CalculaSentimento
import RecoTheme
import Resposta_Audio
import RecoFala
import teste

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
    recognized_text = RecoFala.voiceRecord()
    recognized_text_lower = recognized_text.lower()
    greetings = ["olá", "oi", "oie", "hello", "hi"]
    if recognized_text:
        if recognized_text in greetings:
            resposta = "Olá, qual é o seu nome?"
            Resposta_Audio.AwnswerAudio(resposta)
            recognized_text = RecoFala.voiceRecord()
            if recognized_text:
                prompt = recognized_text
                Nome = teste.RecoNome(prompt)
                Resposta_Audio.AwnswerAudio("Belo nome, tudo bem com você {}?".format(Nome))
        else:
            prompt = recognized_text

            strFeel, feel = CalculaSentimento.CalcFeeling(prompt)
            QuestionType = TipoPergunta.QuestionNeuron().QuestionType(prompt)
            theme = RecoTheme.RecoKeys(prompt)

            # print(strFeel, feel)
            # print(QuestionType)
            # print("Tema: ", theme)
                
# ------------------------------Informações Legais------------------------------
# Projeto iniciado a aproximadamente 1 semana, hoje é dia 26 de agosto de 2023
# Total de horas estará errado pois comeceu a contar ontem a noite, porém é legal pra ter uma idéia
# Total de horas gastas no projeto: 