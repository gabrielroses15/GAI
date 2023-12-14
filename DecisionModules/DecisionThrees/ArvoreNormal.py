def escolhas(prompt: str, resposta: str, promptFormatadoPelaArvoreDeGeografia: bool, testing:bool=True):
    resposta = "Normal tree não obteve resposta"

    if promptFormatadoPelaArvoreDeGeografia == False:
        from DecisionModules.DecisionThrees import ArvoreGeografia as geo
        prompt = geo.Geografia(prompt)

        if prompt[0] == "prompt":
            prompt = prompt[1]

    words = prompt.split()

    from DecisionModules import recoVerbs as verbs
    retornoRecoVerbs = verbs.recoVerbs(words, resposta, testing)
    if retornoRecoVerbs[0] == "resposta":
        return retornoRecoVerbs[1]
    else:
        listaVerbos, contexto = retornoRecoVerbs
        if testing:
            print("LISTA DE VERBOS E CONTEXTO", listaVerbos, contexto)
    from DecisionModules import frasesMapeadas as fMap
    chaves_encontradas = set()
    valores_encontrados = set()
    nomes_encontrados = set()
    pronomes_encontrados = set()

    pronomes = fMap.pronomes()
    names = fMap.nomes()
    data = fMap.dicio(3)

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
