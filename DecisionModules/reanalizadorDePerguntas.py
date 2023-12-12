def analisarPergunta(perguntas, frase: str, dicio: dict, nomes: list, actionVerbs, verbs, testing: bool):
    respostas = []
    from DecisionModules import lightSaber as lSaber
    for pergunta in perguntas:
        indexPerguntas = 0
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
            indexPerguntas += 1
            print("Dev/ answers", respostas)
        except:
            indexPerguntas += 1
            errorQuest = quests[indexPerguntas]
            if errorQuest[0] == " ":
                errorQuest = errorQuest[1:]
            from DecisionModules import fraseInfinitiva as raizes
            from DecisionModules import frasesMapeadas as fMap
            from DecisionModules import StrongVerbs
            errorAnswer = StrongVerbs.StrongVerbs(errorQuest + pergunta + " ele", actionVerbs, dicio, errorQuest.split(), nomes,
                                    raizes.raiz(" ".join(errorQuest.split()), fMap.verbosList()), verbs, testing)
            # nomes encontrados pra ser mais rapido no lugar d nomes
            # Infinitivos menores pq ja foi uma parte e verbos tbm, assim fica mais otimizado!
    return [respostas, errorAnswer]