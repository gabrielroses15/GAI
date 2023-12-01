def PerguntaMedia(prompt, respo):
    respo = respo + " pergunta média também não encontrou resposta!"
    palavras = prompt.split()

    keyWords = ["quantos"]
    substantivos = ["anos", "tinha", "rei"]
    i = 0

    def testar(stop, palavras, substantivos):
        from DecisionModules import frasesMapeadas as fMap
        nomes = fMap.nomes() #PASSAGEM ENTRE CONTROLADORES
        for palavra in palavras:
            if palavra == stop:
                pass
            else:
                w = False
                for sub in substantivos:
                    if palavra == sub:
                        w = False
                        break
                    else:
                        w = True
                if w:
                    for nome in nomes:
                        if nome == palavra:
                            return [palavra]
                    return palavra
        
    for palavra in palavras:
        if palavra in keyWords:
            for sub in substantivos:
                if palavras[i+1] == sub:
                    frase = palavra + " " + palavras[i+1]
                    if frase == "quantos anos":
                        te = testar(palavra, palavras, substantivos)
                        if type(te) == list:
                            return ["idade do {}".format(te[0])]
                        else:
                            return "idade de alguém (não reconhecido({}))".format(palavras[i+2])
        i += 1
    
    # APÓS TERMINAR, N UTILIZAREMOS LISTAS ESTÁTICAS MAS SIM LISTAS VINNDAS DAS MEMÓRIAS.
    # COMO POR EXEMPLO DA MEMÓRIA FMAP, E OUTRAS QUE SERÃO CRIADAS/UPDATEADAS.
    # NOTE QUE APÓS MUITAS MEMÓRIAS SEREM CRIADAS, OS DADOS NÃO MAIS VIRÃO DELAS, MAS SIM DE SEUS-
    # CONROLADORES, POSTERIORMENTE O "CONTROLE" DOS CONTROLADORES SERÁ DADO MAS MÃOS DA IA.