from DecisionModules import recoTheme as Theme
from DecisionModules import caracteres_especiais as special

lastAsks = []
def controller(prompt:str):
    prompt = prompt.lower()
    prompt = special.clearPrompt(prompt)
    words = prompt.split()#cortar as palavras apenas uma vez, poupando RAM
    miniCorretor = {"você": ["vc", "voce", "voçe", "voçê", "tu"],
                    "vo": ["avô", "vovô"],
                    "porshe": ["porche", "porhsi", "pórche", "pórcshi"],
                    "vidro": ["vrido"], "pedra": ["preda"],
                    "são": ["sao"]} #Dicionário pra correção
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
                    "boa noite", "tudo sim e você"]
    #Usar o corretor ortográfico emmm
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
                     "Contente em falar com você!"]
                    #Dps é legal customizar variantes de respostas padrões baseadas nos padrões da pessoa de escrita.
                    #Criar uma trava caso a pessoa seja reconhecida como depressiva, criar tipos mapeados de pessoas assim como personalidades, modos de escrita, modos de pergunta e etc
                    #Alocar os usuários as listas pré prontas de "tipos de pessoas" e caso o usuário não se encaixar em nenhuma lista, entender como ele é e criar uma lista para ele.
                    #Se a pessoa demonstrar sentimentos de depressão ou coisas que podem ser incontroláveis, o bot deve perceber e ativar uma trava para apennas falar sobre assuntos positivos
                    #A trava pode ser apenas um "Por favor, pergunte sobere outro tema ou procure um profissional em saúde mental para auxiliar-lo à encontrar a resposta correta."
    for index, breaks in enumerate(breakPhrases):
        if breaks in prompt:
            resposta = repairAnswers[index]
            return resposta

    resposta = "O contexto da frase escrita não foi compreenndido"

    if len(words) <= 1:
        resposta = "Pergunta pequena demais"
        return resposta

    binaryMapOne = Theme.recognizeTheme(prompt)

    from DecisionModules import runNeurons as run
    resposta = run.runN(binaryMapOne, True, resposta, prompt)

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