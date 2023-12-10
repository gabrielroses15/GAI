def multiVerb(infinitivos, verbs, i):
    try:
        if infinitivos.split()[i + 1] in verbs:
            return True
        if infinitivos.split()[i + 1] in ["a", "e", "o"]:
            if infinitivos.split()[i + 2] in verbs:
                return True
        if infinitivos.split()[i - 2] in ["a", "e", "o"] or infinitivos.split()[i - 2] in verbs and infinitivos.split()[
            i] in verbs:
            return True
        return False
    except:
        return False


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
    contexto_count = {}
    verbosForces = [[], []]

    for valores, frases in dicio.items():
        for valor in valores:
            if frase.count(valor) == 1:
                contexto_count[valor] = contexto_count.get(valor, 0) + 1
            elif frase.count(valor) >= 1:
                contexto_count[valor] = contexto_count.get(valor, 0) + frase.count(valor)

    nomesEncontrados = []
    grupoVerbal = []
    forcaTotal = 0
    i = 0

    for word in infinitivos.split():
        for forcas, raizes in actionVerbs.items():
            if raizes == word:
                if multiVerb(infinitivos, verbs, i):
                    grupoVerbal.append(word)
                    forcaTotal += forcas
                else:
                    if grupoVerbal != []:
                        while "000" in str(forcaTotal):
                            forcaTotal = str(forcaTotal).replace("000", "00")
                        verbosForces[0].append(forcaTotal)
                        verbosForces[1].append(grupoVerbal)
                    verbosForces[0].append(forcas)
                    verbosForces[1].append(raizes)
            for nome in nomes:
                if word == nome and word not in nomesEncontrados:
                    nomesEncontrados.append(word)
                    break
        i += 1

    if grupoVerbal != []:
        while "000" in str(forcaTotal):
            forcaTotal = str(forcaTotal).replace("000", "00")
        verbosForces[0].append(forcaTotal)
        verbosForces[1].append(grupoVerbal)

    if testing == False:
        print("nomesEncontrados:", nomesEncontrados)
        print("verbosForces:", verbosForces)
        i = 0
        for verbos in verbosForces[1]:
            if type(verbos) == list:
                print("Os verbos {} pertencem a pessoa: {} que contém {} de força(importância) na frase".format(
                    ", ".join(verbos), nomesEncontrados[i], verbosForces[0][i]))
                i += 1
                break
            else:
                print("O verbo {} pertence a pessoa: {} que contém {} de força(importância) na frase".format(verbos,
                                                                                                             nomesEncontrados[
                                                                                                                 i],
                                                                                                             verbosForces[
                                                                                                                 0][i]))
                i += 1
                break

    namesForce = {}
    if len(verbosForces[1]) == len(nomesEncontrados):
        count = 0
        for nom in nomesEncontrados:
            namesForce[nom] = verbosForces[0][count]
            count += 1

    if testing == False:
        print(infinitivos)
        print("verbosForces", verbosForces)
        print("nomesEncontrados", nomesEncontrados)
        print("namesForce", namesForce)

    if len(nomesEncontrados) == 1:
        return "reposta", "biografia de " + nomesEncontrados[0]

    if 1 in contexto_count.values():
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
                        if testing == False:
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
        retorno = ""
        b = 0
        d = 0
        j = 0
        while j < len(respostaFinal.split()):
            plvr = respostaFinal.split()[j]
            if respostaFinal.split()[j] == "biografia":
                b += 1
                if b > 1:
                    plvr = ""
            elif respostaFinal.split()[j] == "de":
                d += 1
                if d == 2:
                    plvr = "e"
                elif d > 2:
                    plvr = ","
            retorno = retorno + " " + plvr
            j += 1
        retorno = retorno.replace("  ", " ")
        return "resposta", retorno

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
        indexesMeu = []
        indexesAmigo = []
        indexesMeus = []
        indexesAmigos = []
        contador = 0
        for word in words:
            if word == "meu":
                indexesMeu.append(contador)
            if word == "amigo":
                indexesAmigo.append(contador)
            if word == "meus":
                indexesMeus.append(contador)
            if word == "amigos":
                indexesAmigos.append(contador)
            contador += 1
        if len(indexesMeu) == len(indexesAmigo):
            for index in indexesAmigo:
                for nome in nomes:
                    if nome == words[index + 1]:
                        frase = frase.replace(nome, "").replace("  ", " ")
            print('f', frase)
        else:
            print("uma lista é melhor, me encontre no strongVerbs")

        if len(indexesMeus) == len(indexesAmigos):  # CRIAR LÓGICA PARA CASO A FRASE CONTENHA MEU E MEUS
            print("b")
        else:
            print("uma lista é melhor, me encontre no strongVerbs")

    if nomesEncontrados == []:
        if verbosForces != []:
            if len(verbosForces[1]) == 1:
                return verbResponse(verbosForces[1], words, infinitivos)
        else:
            print("StrongVerbs não encotrou um nome mas encontrou os verbos: {}".format(verbosForces))

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

    if testing == False:
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
                        if testing == False:
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
            retorno = ""
            biografiasEncontradas = 0
            deEcontrados = 0
            index = 0
            while index < len(respostaFinal.split()):
                plvr = respostaFinal.split()[index]
                if respostaFinal.split()[index] == "biografia":
                    biografiasEncontradas += 1
                    if biografiasEncontradas > 1:
                        plvr = ""
                elif respostaFinal.split()[index] == "de":
                    deEcontrados += 1
                    if deEcontrados == 2:
                        plvr = "e"
                    elif deEcontrados > 2:
                        plvr = ","
                retorno = retorno + " " + plvr
                index += 1
            retorno = retorno.replace("  ", " ")
            return "resposta", retorno

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
        indexesMeu = []
        indexesAmigo = []
        indexesMeus = []
        indexesAmigos = []
        contador = 0
        for word in words:
            if word == "meu":
                indexesMeu.append(contador)
            if word == "amigo":
                indexesAmigo.append(contador)
            if word == "meus":
                indexesMeus.append(contador)
            if word == "amigos":
                indexesAmigos.append(contador)
            contador += 1
        if len(indexesMeu) == len(indexesAmigo):
            for index in indexesAmigo:
                for nome in nomes:
                    if nome == words[index + 1]:
                        frase = frase.replace(nome, "").replace("  ", " ")
            print('f', frase)
        else:
            print("uma lista é melhor, me encontre no strongVerbs")

        if len(indexesMeus) == len(indexesAmigos):
            print("b")
        else:
            print("uma lista é melhor, me encontre no strongVerbs")

# print(splitFriends("Meu amigo gregory me recomendou o livro de salmos, que também foi recomendado pelo meu amigo samuel, escrito pelo meu amigo salomão, quem foi ele?".lower()))