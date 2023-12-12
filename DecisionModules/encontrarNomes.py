def encontrarNomes(infinitivos:str, nomes: list):
    nomesEncontrados = []
    for word in infinitivos.split():
        for nome in nomes:
            if word == nome and word not in nomesEncontrados:
                nomesEncontrados.append(word)
                break
    if len(nomesEncontrados) == 1:
        return "biografia de " + nomesEncontrados[0]
    return nomesEncontrados