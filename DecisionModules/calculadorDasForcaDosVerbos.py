def calcularForcaDosVerbos(infinitivos:str, actionVerbs:dict, verbs, nomesEncontrados, testing:bool):
    verbosForces = [[], []]
    grupoVerbal = []
    forcaTotal = 0
    i = 0

    for word in infinitivos.split():
        for forcas, raizes in actionVerbs.items():
            if raizes == word:
                from DecisionModules import reconheceGruposVerbais
                if reconheceGruposVerbais.multiVerb(infinitivos, verbs, i):
                    grupoVerbal.append(word)
                    forcaTotal += forcas
                else:
                    if grupoVerbal != []:
                        while "000" in str(forcaTotal):
                            forcaTotal = str(forcaTotal).replace("000", "00")
                        verbosForces[0].append(forcaTotal)
                        verbosForces[1].append(grupoVerbal)
                        forcaTotal = 0
                        grupoVerbal = []
                        break
                    verbosForces[0].append(forcas)
                    verbosForces[1].append(raizes)
                    break
        i += 1
    if testing:
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
    return verbosForces