def controller(prompt:str, testing=True):
    lastAsks = []
    words = prompt.split()
    if len(words) <= 1:
        resposta = "Pergunta pequena demais."
        return resposta

    prompt = prompt.lower()
    from DecisionModules import caracteres_especiais as special
    prompt = special.clearPrompt(prompt)

    from DecisionModules import respondeFrasesComElogiosEXingamentos as responderElogiosEXingamentos
    respostaXingamentos = responderElogiosEXingamentos.responderElogioEXingamentos(prompt)
    if type(respostaXingamentos) == str:
        return respostaXingamentos

    from DecisionModules import miniCorretorDePrompt
    prompt = miniCorretorDePrompt.corrigirPrompt(prompt, words)

    from DecisionModules import answerBreakPhrases
    respostaParaFrasesComplexas = answerBreakPhrases.verificarFrasesComplexasOuSemResposta(prompt)
    
    if type(respostaParaFrasesComplexas) == list and respostaParaFrasesComplexas[0] == "resposta":
        return respostaParaFrasesComplexas[1]
    
    from DecisionModules import phraseComplexity
    complexity = phraseComplexity.calc(prompt, words)

    resposta = "O contexto da frase escrita não foi compreendido"

    from DecisionModules import recoTheme as Theme
    from DecisionModules import frasesMapeadas as fMap
    binaryMapOne = Theme.recognizeTheme(prompt, complexity=complexity)
    
    if binaryMapOne[0] == "resposta":
        return binaryMapOne[1]

    from DecisionModules import runNeurons as run
    respostas = run.runN(binaryMapOne, resposta, prompt, testing=testing)
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