def recoVerbs(words:list, respo:str, testing:bool=True):
    resposta = 'recoVerbs não reconheceu corretamente, resposta anterior "{}"'.format(respo)
    verbos_encontrados = []
    contexto = ""

    from DecisionModules import frasesMapeadas as fMap
    from DecisionModules import StrongVerbs as sVerbs

    verbosList = fMap.verbosList()
    
    from DecisionModules import  fraseInfinitiva as raizes
    frase_infinitiva = raizes.raiz(" ".join(words), verbosList)

    actionVerbs = {0.62: "recomendar", 0.70: "falar",
                 0.80: "fazer", 0.751: "ir", 0.75: "ter",
                 0.78: "ser", 0.50: "estar", 0.59: "poder", 
                 0.63: "dizer", 0.619: "ver", 0.64: "dar",
                 0.65: "saber", 0.60: "coseguir", 0.785: "escrever",
                 0.81: "produzir", 0.82: "criar"}
    verbs = ["recomendar", "falar", "fazer", "ir", "ter", "ser", "estar",
             "poder", "dizer", "ver", "dar", "saber", "coseguir", "escrever",
            "produzir"]
    
    resposta = sVerbs.StrongVerbs(" ".join(words), actionVerbs, fMap.dicio(3), words, fMap.nomes(), frase_infinitiva, verbs, testing)
    
    if resposta != None:
        if resposta[0] == "resposta":
            return "resposta", resposta

    for word in words:
        for raiz, values in verbosList.items():
            if raiz == word:
                verbos_encontrados.append(raiz)
            for value in values:
                if value == word:
                    verbos_encontrados.append(value)

    prompt = " ".join(words)
    splitPrompt = []
    
    if verbos_encontrados != []:
        splitPrompt.append(prompt.split(verbos_encontrados[0], 1)[0])

        for i in range(len(verbos_encontrados)-1):
            splitPrompt.append(prompt.split(verbos_encontrados[i], 1)[1].split(verbos_encontrados[i+1], 1)[0])
            
        splitPrompt.append(prompt.split(verbos_encontrados[-1], 1)[1])

    from DecisionModules import lightSaber as lSaber

    if lSaber.teste(prompt, fMap.dicio(3), fMap.nomes()) == (None, None):
        print("No context founded.")
    else:
        contexto = " ".join(lSaber.teste(prompt, fMap.dicio(3), fMap.nomes()))
    
    #print(splitPrompt)

    if len(verbos_encontrados) == 0:
        return "resposta: ", resposta
    
    return verbos_encontrados, contexto
