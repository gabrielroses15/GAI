def raiz(frase: str, verbos: list):
    for raiz, verbosList in verbos.items():
        for verbo in verbosList:
            if verbo in frase.split():
                frase = frase.replace(verbo, raiz)
    return frase