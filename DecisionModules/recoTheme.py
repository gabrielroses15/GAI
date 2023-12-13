def recognizeTheme(prompt: str, complexity:int = 0):
    from DecisionModules.Controllers import controladorDeMemorias
    dicioVerbosoBinaryTheme = controladorDeMemorias.returnoDicioVerbosoToBinaryMap(complexity)
    carros = dicioVerbosoBinaryTheme["carros"]
    esportes = dicioVerbosoBinaryTheme["esportes"]
    casa = dicioVerbosoBinaryTheme["casa"]
    perguntaSimples = dicioVerbosoBinaryTheme["perguntaSimples"]
    perguntaMedia = dicioVerbosoBinaryTheme["perguntaMedia"]
    perguntaDificil = dicioVerbosoBinaryTheme["perguntaDificil"]
    financas = dicioVerbosoBinaryTheme["financas"]
    relacionamento = dicioVerbosoBinaryTheme["relacionamento"]
    amor = dicioVerbosoBinaryTheme["amor"]
    sexo = dicioVerbosoBinaryTheme["sexo"]
    antiNSFW = dicioVerbosoBinaryTheme["antiNSFW"]
    informacoesSimples =dicioVerbosoBinaryTheme["informacoesSimples"]
    programacao = dicioVerbosoBinaryTheme["programacao"]
    morte = dicioVerbosoBinaryTheme["morte"]
    arte = dicioVerbosoBinaryTheme["arte"]
    historia = dicioVerbosoBinaryTheme["historia"]
    matematica = dicioVerbosoBinaryTheme["matematica"]
    geografia = dicioVerbosoBinaryTheme["geografia"]
    portugues = dicioVerbosoBinaryTheme["portugues"]
    geometria = dicioVerbosoBinaryTheme["geometria"]
    reflexao = dicioVerbosoBinaryTheme["reflexao"]
    badVibes = dicioVerbosoBinaryTheme["badVibes"]
    solidao = dicioVerbosoBinaryTheme["solidao"]
    amigos = dicioVerbosoBinaryTheme["amigos"]
    NPCTalk = dicioVerbosoBinaryTheme["NPCTalk"]
    Normal = dicioVerbosoBinaryTheme["Normal"]
    temas = [carros, esportes, casa, perguntaSimples, perguntaMedia, perguntaDificil, 
             financas, relacionamento, amor, sexo, antiNSFW, informacoesSimples, programacao,
             morte, arte, historia, matematica, geografia, portugues, geometria, reflexao, badVibes,
             solidao, amigos, NPCTalk, Normal]
    
    palavras = prompt.lower().split()

    BinaryMap = []

    for tema in temas:
        add = 0
        for frase in tema:
            if " " in frase:
                if frase in prompt.lower():
                    add = 1
                    break
            else:
                for palavra in palavras:
                    if palavra == frase:
                        add = 1
        BinaryMap.append(add)

    return BinaryMap