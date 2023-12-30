def StrongVerbs(frase: str, actionVerbs: dict, dicio, words: list, nomes: list, infinitivos: str, verbs: list,
                testing=True):
    infinitivosWords = infinitivos.split()
    from DecisionModules import encontrarNomes
    nomesEncontrados = encontrarNomes.encontrarNomes(infinitivosWords, nomes)

    if type(nomesEncontrados) == str and nomesEncontrados != []:
        return "resposta", nomesEncontrados

    from DecisionModules import calculadorDasForcaDosVerbos as calcVerbsForce
    verbosForces = calcVerbsForce.calcularForcaDosVerbos(infinitivosWords, actionVerbs, verbs, nomesEncontrados, infinitivos ,testing)

    from DecisionModules import calculaForcaDosNomes
    namesForce = calculaForcaDosNomes.calcularForcaDosNomes(verbosForces, nomesEncontrados, testing)

    if testing:
        print(infinitivos)
        
    from DecisionModules import contadorDeContexto
    contexto_count = contadorDeContexto.contarContexto(dicio, frase)

    if contexto_count != {}:#Se a contagem de contexto n for nula
        if 1 in contexto_count.values():#E apenas um contexto for encontrado
            palavraPosContexto = frase.split(str(contexto_count).replace("{", "").replace("'", "").split(":")[0])[1]
            if len(palavraPosContexto.split()) > 1:
                input("Ainda deverá ser implementado")
            else:
                if palavraPosContexto[0] == " ":
                    palavraPosContexto = palavraPosContexto[1:]
                if palavraPosContexto == "eles" or palavraPosContexto == "elas":
                    indexNomes = 0
                    fraseDeRetorno = "biografia de "
                    while indexNomes < len(nomesEncontrados):
                        if (indexNomes + 1) == len(nomesEncontrados):
                            fraseDeRetorno += "e " + nomesEncontrados[indexNomes]
                            return "resposta", fraseDeRetorno
                        else:
                            fraseDeRetorno += nomesEncontrados[indexNomes] + ", "
                        indexNomes +=1

            from DecisionModules import lightSaber as lSaber
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))#Procuramos qm foi e retornamos sua biografia
            return "resposta", resposta
        else:
            from DecisionModules import reanalizadorDePerguntas
            analiseDaPergunta = reanalizadorDePerguntas.analisarPergunta(list(contexto_count.keys()), frase, dicio, nomes, actionVerbs, verbs, testing)
            respostas = analiseDaPergunta[0]
            errorAnswer = analiseDaPergunta[1]
        if len(errorAnswer) == 2:
            errorAnswer = errorAnswer[1]
        for resposta in respostas:
            if resposta != (None, None):
                if len(resposta) == 2:
                    respostas = resposta[0] + " " + resposta[1]
                else:
                    input("TO NO STRONG VERBS, CORRE AQ Q EU ME CAGUEI")
        respostaFinal = respostas + " " + errorAnswer
        if respostaFinal.count("biografia de") > 1:
            from DecisionModules import buscadorBiografias
            return buscadorBiografias.buscarPorBiografiasNaFrase(respostaFinal)

    if len(contexto_count) == 1 and sum(contexto_count.values()) == 1:
        from DecisionModules import lightSaber as lSaber
        if None in lSaber.teste(frase, dicio, nomes):
            input("We are in trouble here!")
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
                from DecisionModules import VerbsResponseGenerator
                return VerbsResponseGenerator.verbResponse(verbosForces[1], words, infinitivos)
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
                    input("StrongVerbs got some problems here")
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
        if ["foram", "eram"] not in infinitivos:  # VERBOS Q INDICAM SINGULAR (caso eles não estejam)
            from DecisionModules import lightSaber as lSaber
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))
            return "resposta", resposta
    else:
        from DecisionModules import reanalizadorDePerguntas
        analiseDaPergunta = reanalizadorDePerguntas.analisarPergunta(list(contexto_count.keys()), frase, dicio, nomes, actionVerbs, verbs, testing)
        respostas = analiseDaPergunta[0]
        errorAnswer = analiseDaPergunta[1]
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
                input("TO NO STRONG VERBS, CORRE AQ Q EU ME CAGUEI")
    if respostas != []:
        respostaFinal = respostas + " " + errorAnswer
        if respostaFinal.count("biografia de") > 1:  # Corrigir o fato de não acessar algumas variáveis
            from DecisionModules import buscadorBiografias
            return buscadorBiografias.buscarPorBiografiasNaFrase(respostaFinal)

    if len(contexto_count) == 1 and sum(contexto_count.values()) == 1:
        from DecisionModules import lightSaber as lSaber
        if None in lSaber.teste(frase, dicio, nomes):
            input("We are in trouble here!")
            return None, None
        else:
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))
            return "resposta", resposta
    else:
        print("Mais de uma frase ou mais de um valor.")
        from DecisionModules import removeNomesDeAmigos
        frase = removeNomesDeAmigos.removerNomesDosAmigos(nomes, words, frase)

# print(splitFriends("Meu amigo gregory me recomendou o livro de salmos, que também foi recomendado pelo meu amigo samuel, escrito pelo meu amigo salomão, quem foi ele?".lower()))