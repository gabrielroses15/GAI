def StrongVerbs(frase: str, actionVerbs: list, dicio, words: list, nomes:list):
    contexto_count = {}

    for valores, frases in dicio.items():
        for valor in valores:
            if frase.count(valor) == 1:
                contexto_count[valor] = contexto_count.get(valor, 0) + 1
            elif frase.count(valor) >= 1:
                contexto_count[valor] = contexto_count.get(valor, 0) + frase.count(valor)

    if len(contexto_count) == 1 and sum(contexto_count.values()) == 1:
        from DecisionModules import lightSaber as lSaber
        if None in lSaber.teste(frase, dicio, nomes):
            print("We are in trouble here!")
            return None, None
        else:
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))
            return "resposta", resposta
        #contar as aparições de valor antes de passar action verbs, otimizando mais ainda!
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
                    if nome == words[index+1]:
                        frase = frase.replace(nome, "").replace("  ", " ")
            print('f', frase)
        else:
            print("uma lista é melhor, me encontre no strongVerbs")
        
        if len(indexesMeus) == len(indexesAmigos):#CRIAR LÓGICA PARA CASO A FRASE CONTENHA MEU E MEUS
            print("b")
        else:
            print("uma lista é melhor, me encontre no strongVerbs")



#print(splitFriends("Meu amigo gregory me recomendou o livro de salmos, que também foi recomendado pelo meu amigo samuel, escrito pelo meu amigo salomão, quem foi ele?".lower()))