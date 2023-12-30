def encontrarNomes(infinitivosWords:list, nomes: list):
    nomesEncontrados = []
    for word in infinitivosWords:#WORDS??
        for nome in nomes:
            if word == nome and word not in nomesEncontrados:
                nomesEncontrados.append(word)
                break
    if len(nomesEncontrados) == 1:
        return "biografia de " + nomesEncontrados[0]
    return nomesEncontrados