def recoVerbs(words:list, respo:str, testing:bool=True):
    resposta = 'recoVerbs não reconheceu corretamente, resposta anterior "{}"'.format(respo)
    verbos_encontrados = []
    contexto = ""

    from DecisionModules import frasesMapeadas as fMap, StrongVerbs as sVerbs, fraseInfinitiva as raizes
    from DecisionModules.Controllers import controladorDeMemorias

    verbosList = fMap.verbosList()

    frase_infinitiva = raizes.raiz(" ".join(words), verbosList)

    actionVerbs = controladorDeMemorias.getActionVerbs()
    verbs = controladorDeMemorias.getInfinitiveVerbs()

    resposta = sVerbs.StrongVerbs(" ".join(words), actionVerbs, fMap.dicio(3), words, fMap.nomes(), frase_infinitiva, verbs, testing)

    if resposta != None:
        if resposta[0] == "resposta":
            return "resposta", resposta

    #ele = 1 nome(+ provável) eles = mais de 1 nome (+ provável)

    for word in words:
        for raiz, values in verbosList.items():
            if raiz == word:
                verbos_encontrados.append(raiz)
            for value in values:
                if value == word:
                    verbos_encontrados.append(value)

    prompt = " ".join(words)
    splitPrompt = []
    try:
        splitPrompt.append(prompt.split(verbos_encontrados[0], 1)[0])

        for i in range(len(verbos_encontrados)-1):
            splitPrompt.append(prompt.split(verbos_encontrados[i], 1)[1].split(verbos_encontrados[i+1], 1)[0])

        splitPrompt.append(prompt.split(verbos_encontrados[-1], 1)[1])

        from DecisionModules import lightSaber as lSaber

        if lSaber.teste(prompt, fMap.dicio(3), fMap.nomes()) == (None, None):
            if testing:
                print("No context founded.")
        else:
            contexto = " ".join(lSaber.teste(prompt, fMap.dicio(3), fMap.nomes()))

        #print(splitPrompt)

        if len(verbos_encontrados) == 0:
            return "resposta: ", resposta

        return verbos_encontrados, contexto
    except:
        return [], ""