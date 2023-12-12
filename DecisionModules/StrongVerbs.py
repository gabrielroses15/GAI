def verbResponse(verbo: str, words: list, fraseInfinitiva: str):
    keyWords = []
    subs = ["livro"]
    conectivos = ["o", "de"]
    for word in words:
        if word == "quem" or word == "quando" or word == "onde" or word == "por que" or word == "pq" or word == "como":
            keyWords.append(word)
        if word not in subs and word not in conectivos:
            context = word
        else:
            context = ""
    if keyWords != [] and len(keyWords) < 2:
        verbDicio = {"escritor": "escrever", "criou": "criar"}
        treatedsCount = 0
        for trated, raizPalavra in verbDicio.items():
            for word in fraseInfinitiva.split():
                if word == raizPalavra:
                    if treatedsCount > 1:
                        input("STRONGVERBS PROBLEMATICO")
                    tratedWord = trated
                    treatedsCount += 1
        if "quem" in words:
            tratedWord = "quem " + tratedWord
        phrase = tratedWord + " " + "o " + context
        return "resposta", phrase
    else:
        input("verbResponse lenght: {}".format(len(keyWords)))
    return ""


def StrongVerbs(frase: str, actionVerbs: dict, dicio, words: list, nomes: list, infinitivos: str, verbs: list,
                testing=True):
    
    from DecisionModules import encontrarNomes
    nomesEncontrados = encontrarNomes.encontrarNomes(infinitivos, nomes)

    if type(nomesEncontrados) == str and nomesEncontrados != []:
        return "resposta", nomesEncontrados

    from DecisionModules import calculadorDasForcaDosVerbos as calcNamesForce
    verbosForces = calcNamesForce.calcularForcaDosVerbos(infinitivos, actionVerbs, verbs, nomesEncontrados, testing)

    from DecisionModules import calculaForcaDosNomes
    namesForce = calculaForcaDosNomes.calcularForcaDosNomes(verbosForces, nomesEncontrados, testing)

    if testing:
        print(infinitivos)

    from DecisionModules import contadorDeContexto
    contexto_count = contadorDeContexto.contarContexto(dicio, frase)

    if contexto_count != {}:#Se a contagem de contexto n for nula
        if 1 in contexto_count.values():#E apenas um contexto for encontrado
            from DecisionModules import lightSaber as lSaber
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))#Procuramos qm foi e retornamos sua biografia
            return "resposta", resposta
        else:
            respostas = []
            perguntas = list(contexto_count.keys())
            from DecisionModules import lightSaber as lSaber
            for pergunta in perguntas:
                k = 0
                try:
                    quests = frase.split(pergunta + " ele")
                    for quest in quests:
                        quest = quest.replace("  ", " ")
                        if quest[0] == " ":
                            quest = quest[1:]
                        if len(quest) > 1:
                            quest = quest + pergunta + " ele"
                            if testing:
                                print("Dev/ quest", quest)
                            respostas.append(lSaber.teste(quest, dicio, nomes))
                    k += 1
                    print("Dev/ answers", respostas)
                except:
                    k += 1
                    errorQuest = quests[k]
                    if errorQuest[0] == " ":
                        errorQuest = errorQuest[1:]
                    from DecisionModules import fraseInfinitiva as raizes
                    from DecisionModules import frasesMapeadas as fMap
                    errorAnswer = StrongVerbs(errorQuest + pergunta + " ele", actionVerbs, dicio, errorQuest.split(), nomes,
                                            raizes.raiz(" ".join(errorQuest.split()), fMap.verbosList()), verbs)
                    # nnms encontrados pra ser mais rapido no lugar d nomes // Infinitivos menores pq ja foi uma parte e verbos tbm, assim fica mais otimizado!
        if len(errorAnswer) == 2:
            errorAnswer = errorAnswer[1]
        for resposta in respostas:
            if resposta != (None, None):
                if len(resposta) == 2:
                    respostas = resposta[0] + " " + resposta[1]
                else:
                    print("TO NO STRONG VERBS, CORRE AQ Q EU ME CAGUEI")
        respostaFinal = respostas + " " + errorAnswer
        if respostaFinal.count("biografia de") > 1:
            from DecisionModules import buscadorBiografias
            return buscadorBiografias.buscarPorBiografiasNaFrase(respostaFinal)

    if len(contexto_count) == 1 and sum(contexto_count.values()) == 1:
        from DecisionModules import lightSaber as lSaber
        if None in lSaber.teste(frase, dicio, nomes):
            print("We are in trouble here!")
            return None, None
        else:
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))
            return "resposta", resposta
        # contar as aparições de valor antes de passar action verbs, otimizando mais ainda!
    else:
        print("Mais de uma frase ou mais de um valor.")
        from DecisionModules import removeNomesDeAmigos
        frase = removeNomesDeAmigos.removerNomesDosAmigos(nomes,words,frase)

    if nomesEncontrados == []:
        if verbosForces != []:
            if len(verbosForces[1]) == 1:
                return verbResponse(verbosForces[1], words, infinitivos)
        else:
            print("StrongVerbs não encotrou um nome nem encontrou os verbos, verbosForce: {}".format(verbosForces))

    i = 0
    for verbos in verbosForces[1]:
        if type(verbos) == list:
            print("Os verbos {} pertencem a pessoa: {} que contém {} de força(importância) na frase".format(
                ", ".join(verbos), nomesEncontrados[i], verbosForces[0][i]))
            i += 1
            break
        else:
            if len(nomesEncontrados) <= i and nomesEncontrados != []:
                print("O verbo {} pertence a pessoa: {} que contém {} de força(importância) na frase".format(verbos,
                                                                                                             nomesEncontrados[
                                                                                                                 i],
                                                                                                             verbosForces[
                                                                                                                 0][i]))
            else:
                print(
                    "O verbo {} pertence a nenhuma pessoa, que contém {} de força(importância) na frase".format(verbos,
                                                                                                                verbosForces[
                                                                                                                    0][
                                                                                                                    i]))
                if len(nomesEncontrados) == 1:
                    return "resposta", "biografia de " + nomesEncontrados[0]
                elif len(nomesEncontrados) == 2:
                    return "resposta", "biografia de " + nomesEncontrados[0] + " e " + nomesEncontrados[1]
                elif len(nomesEncontrados) > 2:
                    fraseDeRetorno = "biografia de "
                    indexNomes = 0
                    for nome in nomesEncontrados:
                        if indexNomes == 0:
                            fraseDeRetorno += nome
                        elif indexNomes == len(nomesEncontrados) - 1:
                            fraseDeRetorno += " e {}".format(nome)
                        else:
                            fraseDeRetorno += ", {}".format(nome)
                        indexNomes += 1
                    return "resposta", "biografia de {}".format(fraseDeRetorno)
                else:
                    print("StrongVerbs got some problems here")
            i += 1
            break

    namesForce = {}
    if len(verbosForces[1]) == len(nomesEncontrados):
        count = 0
        for nom in nomesEncontrados:
            namesForce[nom] = verbosForces[0][count]
            count += 1

    if testing:
        print(infinitivos)
        print("verbosForces", verbosForces)
        print("nomesEncontrados", nomesEncontrados)
        print("namesForce", namesForce)

    if len(nomesEncontrados) == 1:
        return "reposta", "biografia de " + nomesEncontrados[0]

    if 1 in contexto_count.values():
        if ["foram", "eram"] not in infinitivos:  # VERBOS Q INDICAM SINGULAR
            from DecisionModules import lightSaber as lSaber
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))
            return "resposta", resposta
    else:
        respostas = []
        perguntas = list(contexto_count.keys())
        from DecisionModules import lightSaber as lSaber
        for pergunta in perguntas:
            k = 0
            try:
                quests = frase.split(pergunta + " ele")
                for quest in quests:
                    quest = quest.replace("  ", " ")
                    if quest[0] == " ":
                        quest = quest[1:]
                    if len(quest) > 1:
                        quest = quest + pergunta + " ele"
                        if testing:
                            print("Dev/ quest", quest)
                        respostas.append(lSaber.teste(quest, dicio, nomes))
                k += 1
                print("Dev/ answers", respostas)
            except:
                k += 1
                errorQuest = quests[k]
                if errorQuest[0] == " ":
                    errorQuest = errorQuest[1:]
                from DecisionModules import fraseInfinitiva as raizes
                from DecisionModules import frasesMapeadas as fMap
                errorAnswer = StrongVerbs(errorQuest + pergunta + " ele", actionVerbs, dicio, errorQuest.split(), nomes,
                                          raizes.raiz(" ".join(errorQuest.split()), fMap.verbosList()), verbs, testing)
                # nnms encontrados pra ser mais rapido no lugar d nomes // Infinitivos menores pq ja foi uma parte e verbos tbm, assim fica mais otimizado!
    try:
        if len(errorAnswer) == 2:
            errorAnswer = errorAnswer[1]
    except:
        pass
    for resposta in respostas:
        if resposta != (None, None):
            if len(resposta) == 2:
                respostas = resposta[0] + " " + resposta[1]
            else:
                print("TO NO STRONG VERBS, CORRE AQ Q EU ME CAGUEI")
    if respostas != []:
        respostaFinal = respostas + " " + errorAnswer
        if respostaFinal.count("biografia de") > 1:  # Corrigir o fato de não acessar algumas variáveis
            from DecisionModules import buscadorBiografias
            return buscadorBiografias.buscarPorBiografiasNaFrase(respostaFinal)

    if len(contexto_count) == 1 and sum(contexto_count.values()) == 1:
        from DecisionModules import lightSaber as lSaber
        if None in lSaber.teste(frase, dicio, nomes):
            print("We are in trouble here!")
            return None, None
        else:
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))
            return "resposta", resposta
    else:
        print("Mais de uma frase ou mais de um valor.")
        from DecisionModules import removeNomesDeAmigos
        frase = removeNomesDeAmigos.removerNomesDosAmigos(nomes, words, frase)

# print(splitFriends("Meu amigo gregory me recomendou o livro de salmos, que também foi recomendado pelo meu amigo samuel, escrito pelo meu amigo salomão, quem foi ele?".lower()))