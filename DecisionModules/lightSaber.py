def teste(frase:str, data, names):
    frase = frase.lower()
    valor_proximo = None
    nome_proximo = None

    for chaves, valor in data.items():
        for key in chaves:
            if key in frase:
                start_idx = frase.split().index(key.split()[0])

                # palavra anterior
                if start_idx > 0:
                    palavra_anterior = frase.split()[start_idx - 1]
                    if palavra_anterior in names:
                        valor_proximo = valor
                        nome_proximo = palavra_anterior

                # Palavra seguinte à chave
                if start_idx < len(frase.split()) - 1:
                    palavra_seguinte = frase.split()[start_idx + len(key.split())]
                    if palavra_seguinte in names:
                        valor_proximo = valor
                        nome_proximo = palavra_seguinte

    return valor_proximo, nome_proximo