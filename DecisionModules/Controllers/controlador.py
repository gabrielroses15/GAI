def controller(prompt:str, testing=True):
    lastAsks = []
    words = prompt.split()  # cortar as palavras apenas uma vez, poupando RAM
    if len(words) <= 1:
        resposta = "Pergunta pequena demais."
        return resposta

    prompt = prompt.lower()
    from DecisionModules import caracteres_especiais as special
    prompt = special.clearPrompt(prompt)
    pronomes = ["você", "voce", "vc", "tu", "gai"]
    eh = ["é", "eh", "éh", "ehh", "éhh"]
    elogios = ["demais", "dimais", "de mais", "dms", "di mais", "incrivel", "incrível", "espetacular", "indescritível", "indescritivel", "insano", "esbelto", "magnífico", "magnificiente", "admirável", "exemplar", "inteligete", "foda"]
    xingamentos = ["um merda", "um bosta", "horrível", "zoado", "hororroso", "horrendo", "um desgraçado", "desgraçado", "um fudido", "um fodido", "fudido", "fodido"]

    for pronome in pronomes:
        for e in eh:
            for elogio in elogios:
                frase = pronome + " " + e + " " + elogio
                if frase in prompt:
                    resposta = "Obrigado, vc que é {}, além de ser minha inspiração!".format(elogio)
                    return resposta
            for xingamento in xingamentos:
                frase = pronome + " " + e + " " + xingamento
                if frase in prompt:
                    resposta = "Ei, não chame as pessoas de {}, isto não é legal!".format(xingamento)
                    return resposta

    miniCorretor = {"você": ["vc", "voce", "voçe", "voçê", "tu"],
                    "vo": ["avô", "vovô"],
                    "porshe": ["porche", "porhsi", "pórche", "pórcshi"],
                    "vidro": ["vrido"], "pedra": ["preda"],
                    "são": ["sao"],
                    "qual é o seu nome": ["qual o seu nome", "qual e o seu nome",
                                          "qual é o seu nm", "cual é o seu nome",
                                          "cual e o seu nome", "cual é u seu nome",
                                          "cual e u seu nome", "qual é seu nome",
                                          "qual seu nome"],
                    "napoleão": ["napoleao", "nápoleao", "nápoleão", "napoliao", "napoleão bonaparte", "bonaparte"]} #Dicionário pra correção #"te achei {}"
    for valor, palavras in miniCorretor.items():
        for palavra in palavras:
            for word in words:
                if word == palavra:
                    prompt = prompt.lower().replace(palavra, valor)

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
                     # Pode trocar o "jantar em família" por alguma informação que o bot entendeu que é importante para o usuário
                     "Se meu sentido é responder suas perguntas, talvez o seu seja perguntar.",
                     "Ei, isto não estava no roteiro.",
                     "Hmmm, carregando?", "São tantos sentidos, que não posso resumi-los em palavras.",
                     "bom dia, tudo bem?", "boa tarde, tudo bem?", "boa noite, tudo bem?",
                     "Contente em falar com você!", "Meu nome é GAI!"]
                     #Dps é legal customizar variantes de respostas padrões baseadas nos padrões da pessoa de escrita.
                     #Criar uma trava caso a pessoa seja reconhecida como depressiva, criar tipos mapeados de pessoas assim como personalidades, modos de escrita, modos de pergunta e etc
                     #Alocar os usuários as listas pré prontas de "tipos de pessoas" e caso o usuário não se encaixar em nenhuma lista, entender como ele é e criar uma lista para ele.
                     #Se a pessoa demonstrar sentimentos de depressão ou coisas que podem ser incontroláveis, o bot deve perceber e ativar uma trava para apennas falar sobre assuntos positivos
                     #A trava pode ser apenas um "Por favor, pergunte sobere outro tema ou procure um profissional em saúde mental para auxiliar-lo à encontrar a resposta correta."
    ResponsesLists = []
    AsksLists = []
    for index, breaks in enumerate(breakPhrases):
        if breaks in prompt:
            resposta = repairAnswers[index] #TBM TEM Q RESPONDER SE A PERGUNTA FOR GRANDE MAS CONTIVER OU RESPODER TBM MSM Q HAJA 2 PERGUNTAS, OU VÁRIAS PERGUNTAS
            #SENDO A VER OU N
            ResponsesLists.append(resposta)
            AsksLists.append(breaks)
            #return resposta

    if len(ResponsesLists) > 1:
        import geraRespostas as generateAnswer
        generateAnswer.gerarRespostas(ResponsesLists, AsksLists)

    resposta = "O contexto da frase escrita não foi compreendido"
    from DecisionModules import recoTheme as Theme
    from DecisionModules import frasesMapeadas as fMap
    binaryMapOne = Theme.recognizeTheme(prompt, verbos=fMap.verbosList(), nomes=fMap.nomes())

    if binaryMapOne[0] == "resposta":
        return binaryMapOne[1]

    from DecisionModules import runNeurons as run

    respostas = run.runN(binaryMapOne, True, resposta, prompt, testing=testing)
    if type(respostas) == list:
        for answer in respostas:
            if answer != "Sem resposta dada ao runNeurons":
                return answer
        if len(resposta) == 2:
            resposta = resposta[2]
    elif respostas != "Sem resposta dada ao runNeurons":
        resposta = respostas

    #Lógica pra entender e se lembrar de como o usuário fala
    maxMemory = 98
    if len(lastAsks) < maxMemory:
        neuronios = ["carros", "esportes", "casa", "perguntaSimples", "perguntaMedia", "perguntaDificil",
             "financas", "relacionamento", "amor", "sexo", "antiNSFW", "informacoesSimples", "programacao",
             "morte", "arte", "historia", "matematica", "geografia", "portugues", "geometria", "reflexao", "badVibes",
             "solidao", "amigos", "NPCTalk", "Normal"]
        neuronios_usados = []
        index = 0
        for numero in binaryMapOne:
            if numero == 1:
                neuronios_usados.append(neuronios[index])
            index += 1
        lastAsks.append({'prompt': prompt, 'resposta': resposta, 'neuroniosUsados': neuronios_usados, 'words': words})
    else:
        contador = {}
        prepo = ["a", "afora", "após", "antes", "até", "com", "como", "conforme", "consoante",
                 "contra", "conforme", "consoante", "de", "desde", "durante", "em", "entre",
                 "mediante", "para", "perante", "por", "salvo", "segundo", "senão", "sob",
                 "sobre", "trás", "através", "além", "ante", "aquém", "atrás", "aonde", "após",
                 "aquando", "a par", "à espera", "à medida que", "à medida de", "à moda de", "a par de",
                 "à proporção que", "à queima-roupa", "à roda de", "à semelhança de", "à sombra de",
                 "à volta de", "acerca de", "além de", "ao", "ao lado de", "ao longe de", "ao pé de",
                 "ao redor de", "ao rés de", "ao tempo de", "até quando", "abaixo de", "acima de",
                 "afora", "antes de", "ao encontro de", "ao invés de", "ao preço de", "à espera de",
                 "a fim de", "a par", "a propósito de", "a respeito de", "à roda de", "a salvo de",
                 "a semelhança de", "a serviço de", "a troco de","a uma", "a uma distância de",
                 "a uma quadra de", "a uma volta de","a um canto de", "a um tempo", "a vau",
                 "com a condição de","com a finalidade de", "com base em", "com referência a","contra a",
                 "debaixo de", "de baixo de", "de encontro a", "de encontro com","de encontro a",
                 "de harmonia com", "de maneira a", "de maneira que", "de mãos dadas com","de par com",
                 "de perto de", "de resto", "de sabor de", "de sorte que", "é", "o", "da", "um", "e",
                 "do", "da", "de", "di", "do", "du"]
        for ask in lastAsks:
            words = ask['words']
            for word in words:
                if word not in prepo:
                    if word in contador:
                        contador[word] += 1
                    else:
                        contador[word] = 1
        palavras_ordenadas = sorted(contador, key=contador.get, reverse=True)

        top5 = palavras_ordenadas[:5]

        print("As cinco palavras mais frequentes são:")
        for palavra in top5:
            print(f"{palavra}: {contador[palavra]} vezes")

        # import json
        # with open('perguntas.txt', 'w') as arquivo:
        #     json.dump(lastAsks, arquivo, indent=4)
        #     print("Dados salvos em perguntas.txt")
    #Lógica pra entender e se lembrar de como o usuário fala

    if type(resposta) == list:
        resposta = "\n".join(resposta)

    # if resposta == "Sem resposta dada ao runNeurons":#pip uninstall googlesearch-python
    #     print('pesquisarei "{}"'.format(prompt))

    return resposta