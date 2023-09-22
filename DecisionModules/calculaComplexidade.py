from DecisionModules import caracteres_especiais as special

def CalcComplex(prompt: str, tipos):
    complexidade = 0
    palavras = prompt.split()
    if len(palavras) > 1:
        verificacao = True
    else:
        verificacao = False
        
    if verificacao:
        num_palavras = len(palavras)
        prompt, tipos = special.specialCharacters(prompt, tipos)
        if num_palavras == 2:
            complexidade = 1
        elif num_palavras == 3:
            complexidade = 2
        elif num_palavras == 4:
            complexidade = 3
        elif num_palavras == 5:
            complexidade = 4
        elif num_palavras == 6:
            complexidade = 5
        elif num_palavras == 7:
            complexidade = 6
        elif num_palavras == 8:
            complexidade = 7
        elif num_palavras == 9:
            complexidade = 8
        elif num_palavras == 10:
            complexidade = 9
        elif num_palavras < 10:
            complexidade = 10
        return complexidade # N precisa ser de 0 a 100, pd ser d 10 em 10, sendo os 10 primeiros aq e os outros 90 dentro de extrair contexto, usando x como 0, e indo x + 1 até 10, e chamando o calculca complexidade com x valendo 20
    else:
        return "Por favor reformule." #Frases menores podem ser difíceis "o que é a vida"