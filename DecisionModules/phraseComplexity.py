def calc(prompt:str, words:list, rounds:int = 0):
    maxTotalComplexity = 108
    wordIndex = 0
    complexity = 0

    dicioComplexity = {("quem", "quando", "como", "onde", "pq"): 1}
    
    if rounds > 1:#Lógicas q incluem mais análises para rounds maiores
        dicioComplexity["testar"] = 3#Lógicas q incluem mais análises para rounds maiores

    for word in words:
        wordIndex += 1
        for keys, value in dicioComplexity.items():
            if type(keys) == tuple:
                for key in keys:
                    if key == word:
                        complexity += value
                        break
            elif type(keys) == str:
                if keys == word:
                    complexity += value
            else:
                print("Tipo sus aq em phraseComplexity")
        if complexity == rounds+10:
            try:
                newWords = words[wordIndex:]
            except:
                print("erro na geração de newWords")
            retorno = calc(" ".join(newWords), newWords, rounds+1)
            if type(retorno) == int:
                complexity += retorno
                rounds += 1
                return complexity
            if type(retorno) == list:
                complexity += retorno[0]
                rounds += retorno[1]
                complexity += retorno[0]
                return [complexity, rounds]
        if complexity > maxTotalComplexity:
            return [complexity]
    return complexity