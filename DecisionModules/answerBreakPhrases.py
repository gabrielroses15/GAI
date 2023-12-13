def verificarFrasesComplexasOuSemResposta(prompt: str):
    breakPhrases = ["o que é a vida", "o que e a vida", "o q é a vida", "o q e a vida", "oq e a vida",
                    "oq é a vida", "como é morrer", "como e morrer", "cm é morrer", "cm e morrer",
                    "sentido da vida", "qual o sentido da vida", "qual é o sentido da vida",
                    "qual e o sentido da vida", "qual é o sentido de viver",
                    "qual e o sentido viver", "qual o sentido de viver", "bom dia", "boa tarde",
                    "boa noite", "tudo sim e você", "qual é o seu nome", "você é legal"]
    repairAnswers = ["Uma sucessão de fatos.", "Uma busca energética por mais energia",
                     "Também estou tentando entender",
                     "Não sei ao certo, mas garanto que a resposta deve estar ligada a uma busca incessante por ser feliz, quando na verdade já somos.",
                     "Esta é uma bela pergunta, aconselho-o a perguntar para um profissional de saude mental, se cuide :)",
                     "Nossa, nunca parei pra pensar nisso, você deveria fazer o mesmo",
                     "Morrer é uma experiência única.", "Nao sei te responder esta pergunta, que tal tentar outra?",
                     "Desculpe, eu não posso te ajudar com isto.", "Você pode mudar de assunto?",
                     "O sentido da vida é ser feliz.",
                     "O sentido da vida é complexo demais para se resumir em 13Bi de frases",
                     "Hmmm talvez... jantar em família?",
                     "Se meu sentido é responder suas perguntas, talvez o seu seja perguntar.",
                     "Ei, isto não estava no roteiro.",
                     "Hmmm, carregando?", "São tantos sentidos, que não posso resumi-los em palavras.",
                     "bom dia, tudo bem?", "boa tarde, tudo bem?", "boa noite, tudo bem?",
                     "Contente em falar com você!", "Meu nome é GAI!"]
    ResponsesLists = []
    AsksLists = []
    for index, breaks in enumerate(breakPhrases):
        if breaks in prompt:
            resposta = repairAnswers[index]
            ResponsesLists.append(resposta)
            AsksLists.append(breaks)
    if len(ResponsesLists) > 1:
        import geraRespostas as generateAnswer
        generateAnswer.gerarRespostas(ResponsesLists, AsksLists)
    return ""