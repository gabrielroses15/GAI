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
        else:
            resposta = " ".join(lSaber.teste(frase, dicio, nomes))
            return "resposta", resposta
        #contar as aparições de valor antes de passar action verbs, otimizando mais ainda!
    else:
        print("Mais de uma frase ou mais de um valor.")


#print(splitFriends("Meu amigo gregory me recomendou o livro de salmos, que também foi recomendado pelo meu amigo samuel, escrito pelo meu amigo salomão, quem foi ele?".lower()))