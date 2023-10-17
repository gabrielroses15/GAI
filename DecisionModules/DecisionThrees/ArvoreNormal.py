def escolhas(prompt:str, resposta:str):
    resposta = "Normal tree não obteve resposta"
    breakPhrases = ["o que é a vida", "o que e a vida", "o q é a vida", "o q e a vida", "oq e a vida",
                    "oq é a vida", "como é morrer", "como e morrer", "cm é morrer", "cm e morrer",
                    "sentido da vida", "qual o sentido da vida", "qual é o sentido da vida",
                    "qual e o sentido da vida", "qual é o sentido de viver",
                    "qual e o sentido viver"]
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
                     "Ei, isto não estava no roteiro",
                     "Hmmm, carregando?"]

    for index, breaks in enumerate(breakPhrases):
        if breaks in prompt:
            resposta = repairAnswers[index]
            return resposta

    from DecisionModules.DecisionThrees import ArvoreGeografia as geo

    prompt = geo.Geografia(prompt)

    if prompt[0] == "prompt":
        prompt = prompt[1]

    words = prompt.split()

    from DecisionModules import recoVerbs as verbs
    if verbs.recoVerbs(words, resposta)[0] == "resposta":
        return verbs.recoVerbs(words, resposta)[1]
    else:
        listaVerbos, contexto = verbs.recoVerbs(words, resposta)
    from DecisionModules import frasesMapeadas as fMap
    chaves_encontradas = set()
    valores_encontrados = set()
    nomes_encontrados = set()
    pronomes_encontrados = set()

    pronomes = fMap.pronomes()
    names = fMap.nomes()
    data = fMap.dicio(3)

    if any(especial in prompt for especial in ["?", ".", "!", ",", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "-", "+", "=", "*", "&", "%", "$", "#", "@", "~", "`", "^"]):
        from DecisionModules import caracteres_especiais as special
        prompt = special.clearPrompt(prompt)
    for chaves, valor in data.items():
        for name in names:
            for word in words:
                if name == word:
                    nomes_encontrados.add(name)
                    for key in chaves:
                        if key in prompt:
                            chaves_encontradas.add(key)
                            valores_encontrados.add(valor)

    for pronome in pronomes:
        for word in words:
            if pronome == word:
                pronomes_encontrados.add(pronome)

    #print("ABCD pronomes encontrados:{}\n nomes encontrados:{}\n chaves e valores encontrados: {} {} ABCD".format(pronomes_encontrados, nomes_encontrados, chaves_encontradas, valores_encontrados))

    if valores_encontrados:
        resposta = ""
        resposta += next(iter(valores_encontrados))

        if nomes_encontrados:
            resposta += " " + ", ".join(nomes_encontrados)

    return "resposta", resposta
