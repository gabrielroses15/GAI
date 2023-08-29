import RecoFala
import Resposta_Audio

def BuildAwnswer(texto):
    pergunta = texto
    
    saudacoes = ["oi", "oie", "olá", "alo", "hello", "alou"]
    
    def responder(resposta):
        Resposta_Audio.AwnswerAudio(resposta)
    
    def perguntar():
        pergunta = RecoFala.voiceRecord(False)
        return pergunta
    
    for saudacao in saudacoes:
        if pergunta in saudacao:
            resposta = "Olá, qual seu nome?"
            responder(resposta)
            
            nome = perguntar()
            resposta = "Que legal, {} é um belo nome, quantos anos você tem? ah, fale apenas os números.".format(nome)
            responder(resposta)
            
            anos = perguntar()
            anos = int(anos)
            if anos >= 18:
                resposta = "Nossa que legal você já tem {} anos, e isto te torna legalmente de maior. Parabéns, infelizmente meu banco de dados só suporta a nossa conversa até aqui. se possível me ajude aprender mais, para que um dia eu possa me tornar tão grande e forte quanto você, até breve!".format(anos)
                responder(resposta)
            if anos < 18:
                resposta = "Nossa que legal você já tem {} anos, e isto te torna legalmente de menor. infelizmente meu banco de dados só suporta a nossa conversa até aqui. se possível me ajude aprender mais, para que um dia eu possa me tornar tão grande e forte quanto você, até breve!".format(anos)
                responder(resposta)
            break