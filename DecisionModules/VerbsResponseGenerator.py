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