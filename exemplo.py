palavrasChave = ["quem", "quando", "onde", "que", "quantos"]

def separador1(frase: str):
    palavras = frase.lower().split()
    primeiro = False
    perguntasEncontradas = []

    for palavra in palavras:
        for chave in palavrasChave:
            if palavra == chave and "e" in palavras:
                if primeiro:
                    perguntasEncontradas.append(palavras[palavras.index(palavra):])
                primeiro = True

    return perguntasEncontradas


perguntas = separador1("Quem foi salomão, onde ele nasceu e quando ele nasceu")
print(perguntas)