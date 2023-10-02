def singPlurar(prompt, retorno:bool = True):
    dicioPron = {("ele", "dele", "ela", "dela"): "Singular", ("eles", "deles", "elas", "delas", "nós", "vós"): "plural"}
    words = prompt.split()
    for word in words:
        for keys, value in dicioPron.items():
            for key in keys:
                if key == word:
                    if retorno == True:
                        return value
                    else:
                        return word

def intercalar_busca(frase1:str, frase2:str, listbusca, nomes:bool = True): #Criando tipos de busca pra transformar
    #em um neurônio
    if nomes:
        nomesValidados = []
        palavras = frase1.lower().split()[::-1]  # Separa a primeira frase em palavras e inverte a ordem
        for item in listbusca:
            for palavra in palavras:
                if palavra == item:
                    nomesValidados.append(palavra)
                    break
            else:
                for palavra in frase2.lower().split():
                    if palavra == item:
                        break
        resposta = "biografia de "
        first = False
        for nome in nomesValidados:
            if first:
                resposta = resposta + " e " + nome
            else:
                resposta = resposta + nome
                first = True
        return resposta
    else:
        print("ué")