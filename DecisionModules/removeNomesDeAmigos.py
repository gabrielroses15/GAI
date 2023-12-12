def removerNomesDosAmigos(nomes:list, words:list, frase):
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
    if len(indexesMeu) > 0 and len(indexesAmigo) > 0:
        if len(indexesMeu) == len(indexesAmigo):
            for index in indexesAmigo:
                for nome in nomes:
                    if nome == words[index + 1]:
                        frase = frase.replace(nome, "").replace("  ", " ")
        else:
            print("uma lista é melhor, me encontre no removeNomesDeAmigos")
    if len(indexesMeus) > 0 and len(indexesAmigos) > 0:
        if len(indexesMeus) == len(indexesAmigos):  # CRIAR LÓGICA PARA CASO A FRASE CONTENHA MEU E MEUS
            print("meus amigos presentes...")
        else:
            print("uma lista é melhor, me encontre no removeNomesDeAmigos")
    return frase