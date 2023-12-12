def contarContexto(dicio:dict, frase: str):
    contexto_count = {}
    for valores, frases in dicio.items():
        for valor in valores:
            if frase.count(valor) == 1:
                contexto_count[valor] = contexto_count.get(valor, 0) + 1
            elif frase.count(valor) >= 1:
                contexto_count[valor] = contexto_count.get(valor, 0) + frase.count(valor)
    return contexto_count