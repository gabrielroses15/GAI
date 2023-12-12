def calcularForcaDosNomes(verbosForces: list, nomesEncontrados: list, testing: bool):
    namesForce = {}
    if len(verbosForces[1]) == len(nomesEncontrados):
        count = 0
        for nom in nomesEncontrados:
            namesForce[nom] = verbosForces[0][count]
            count += 1
    if testing:
        print("namesForce", namesForce)
    return namesForce