breakPhrases = ["o que é a vida", "o que e a vida", "o q é a vida", "o q e a vida", "oq e a vida", 
                "oq é a vida", "como é morrer", "como e morrer", "cm é morrer", "cm e morrer", 
                "sentido da vida", "qual o sentido da vida", "qual é o sentido da vida", 
                "qual e o sentido da vida", "qual é o sentido de viver", "qual e o sentido viver"]#da pra usar um dicionario de palavras, pra otimizar o tempo gasto tbm

repairAnswers = ["Uma sucessão de fatos.", "Uma busca energética por mais energia", 
                 "Também estou tentando entender","Não sei ao certo, mas garanto que a resposta deve estar ligada a uma busca incessante por ser feliz, quando na verdade já somos.",
                 "Esta é uma bela pergunta, aconselho-o a perguntar para um profissional de saude mental, se cuide :)",
                 "Nossa, nunca parei pra pensar nisso, você deveria fazer o mesmo",
                 "Morrer é uma experiência única.", "Nao sei te responder esta pergunta, que tal tentar outra?",
                 "Desculpe, eu não posso te ajudar com isto.", "Você pode mudar de assunto?", "O sentido da vida é ser feliz.",
                 "O sentido da vida é complexo demais para se resumir em 13Bi de frases", "Hmmm talvez... jantar em família?", #Pode trocar o "jantar em família" por alguma informação que o bot entendeu que é importante para o usuário
                 "Se meu sentido é responder suas perguntas, talvez o seu seja perguntar.", "Ei, isto não estava no roteiro",
                 "Hmmm, carregando?"]#Dps é legal customizar variantes de respostas padrões baseadas nos padrões da pessoa de escrita. 
                 #Criar uma trava caso a pessoa seja reconhecida como depressiva, criar tipos mapeados de pessoas assim como personalidades, modos de escrita, modos de pergunta e etc
                 #Alocar os usuários as listas pré prontas de "tipos de pessoas" e caso o usuário não se encaixar em nenhuma lista, entender como ele é e criar uma lista para ele. 
                 #Se a pessoa demonstrar sentimentos de depressão ou coisas que podem ser incontroláveis, o bot deve perceber e ativar uma trava para apennas falar sobre assuntos positivos
                 #A trava pode ser apenas um "Por favor, pergunte sobere outro tema ou procure um profissional em saúde mental para auxiliar-lo à encontrar a resposta correta."

def CalcComplex(prompt: str):
    for index, breaks in enumerate(breakPhrases):
        if breaks in prompt:
            resposta = repairAnswers[index]
            return resposta

    complexidade = 0
    palavras = prompt.split()
    if len(palavras) > 1:
        verificacao = True
    else:
        verificacao = False
        
    if verificacao:
        num_palavras = len(palavras)
        if num_palavras == 2:
            complexidade = 1
        elif num_palavras == 3:
            complexidade = 2
        elif num_palavras == 4:
            complexidade = 3
        elif num_palavras == 5:
            complexidade = 4
        elif num_palavras == 6:
            complexidade = 5
        elif num_palavras == 7:
            complexidade = 6
        elif num_palavras == 8:
            complexidade = 7
        elif num_palavras == 9:
            complexidade = 8
        elif num_palavras == 10:
            complexidade = 9
        elif num_palavras < 10:
            complexidade = 10
        return complexidade # N precisa ser de 0 a 100, pd ser d 10 em 10, sendo os 10 primeiros aq e os outros 90 dentro de extrair contexto, usando x como 0, e indo x + 1 até 10, e chamando o calculca complexidade com x valendo 20
    else:
        return "Por favor reformule." #Frases menores podem ser difíceis "o que é a vida"