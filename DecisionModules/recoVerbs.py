def recoVerbs(words:list, respo:str):
    resposta = 'recoVerbs não reconheceu corretamente, resposta anterior "{}"'.format(respo)
    verbos_encontrados = []
    contexto = ""

    verbosList = {
    "fazer": ["faço", "fazia", "fazeis", "feito"],
    "ir": ["vou", "ia", "ides"],
    "ter": ["tenho", "tinha", "tendes"],
    "ser": ["sou", "era", "sereis"],
    "estar": ["estou", "estava", "esteis"],
    "poder": ["posso", "podia", "podeis"],
    "dizer": ["digo", "dizia", "dizeis"],
    "ver": ["vejo", "via", "veis"],
    "dar": ["dou", "dava", "dais"],
    "saber": ["sei", "sabia", "sabeis"],
    "coseguir": ["cosegue", "conseguia", "consegues"],
    "escrever": ["escreveu", "escrito", "escrevido"],
    "produzir": ["produzido"],
    "recomendar": ["recomendou", "recomendaste", "recomendado"],
    "falar": ["falou", "fala", "falaste"]
    }

    for word in words:
        for raiz, values in verbosList.items():
            if raiz == word:
                verbos_encontrados.append(raiz)
            for value in values:
                if value == word:
                    verbos_encontrados.append(value)

    prompt = " ".join(words)
    splitPrompt = []
    
    splitPrompt.append(prompt.split(verbos_encontrados[0], 1)[0])

    for i in range(len(verbos_encontrados)-1):
        splitPrompt.append(prompt.split(verbos_encontrados[i], 1)[1].split(verbos_encontrados[i+1], 1)[0])
        
    splitPrompt.append(prompt.split(verbos_encontrados[-1], 1)[1])

    from DecisionModules import frasesMapeadas as fMap
    from DecisionModules import lightSaber as lSaber

    contexto = " ".join(lSaber.teste(prompt, fMap.dicio(3), fMap.nomes()))
    
    #print(splitPrompt)

    if len(verbos_encontrados) == 0:
        return "resposta: ", resposta
    
    return verbos_encontrados, contexto